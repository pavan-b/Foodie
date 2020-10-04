from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import requests

from threading import Thread


class RestaurantForm(FormAction):
	"""custom form action"""

	def name(self):
		"""Unique identifier of the form"""
		return "restaurant_form"

	@staticmethod
	def filter_restaurants_based_on_budget(r, avg_budget):
		if avg_budget == 1:
			new_restaurants=filter(lambda res: res['restaurant']['average_cost_for_two'] < 300,r)
			return new_restaurants
		elif avg_budget == 2:
			new_restaurants=filter(lambda res: (res['restaurant']['average_cost_for_two'] >=  300) and (res['restaurant']['average_cost_for_two'] <  700),r)
			return new_restaurants
		else:
			new_restaurants=filter(lambda res: res['restaurant']['average_cost_for_two'] >=  700,r)
			return new_restaurants
	
	@staticmethod
	def check_if_location_exists(loc):
		config={ "user_key":"9edebdcfe4d2361976e981ee620d0f88"}
		zomato = zomatopy.initialize_app(config)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		if len(d1["location_suggestions"]) == 0 :
			return False
		else:
			return True

	

	@staticmethod
	def required_slots(tracker):
		"""A list of required slots that the form has to fill"""


		return ["location","cuisine",
					"avg_budget"]

	def submit(self,dispatcher,
        tracker,domain):
		"""Define what the form has to do
			after all required slots are filled"""


		config={ "user_key":"9edebdcfe4d2361976e981ee620d0f88"}
		zomato = zomatopy.initialize_app(config)
		
		cuisines_dict={'American':1,'Chinese':25,'Mexican':73,'Italian':55,'North Indian':50,'Thai':95,'South Indian':85}
		prices_dict={"0 - 300":1,"300 - 700":2,"More than 700":3}

		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		avg_budget = tracker.get_slot('avg_budget')
		avg_budget = prices_dict.get(avg_budget)
		print(loc)
		print(cuisine)
		print(avg_budget)
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		results=zomato.restaurant_search_ordered_by_ratings("", lat, lon, str(cuisines_dict.get(cuisine)))
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			dispatcher.utter_template("utter_show_results",tracker)
			new_r=RestaurantForm.filter_restaurants_based_on_budget(d['restaurants'],avg_budget)
			counter=0
			for i in new_r:
				counter+=1
				if counter <= 5:
					response=response+ str(counter)+". "+ i['restaurant']['name']+ " in "+ i['restaurant']['location']['address']+" has been rated "+i['restaurant']['user_rating']['aggregate_rating']+". And the average price for two people here is: "+str(i['restaurant']['average_cost_for_two'])+" Rupees."+"\n"
					response=response+"------------------------"+"\n"
		if response:
			dispatcher.utter_message(response)
		else:
			dispatcher.utter_message("no results")
		return [SlotSet('response', response)]

	@staticmethod
	def check_location_validity(loc):
		cities=open('cities.txt')
		valid_cities=''
		for i in cities:
			valid_cities=valid_cities+i
		valid_cities=valid_cities.split(',')
		for city in valid_cities:
			if loc.lower() == city.lower():
				return True
		return False



	def validate_location(
		self,
		value,
		dispatcher,
		tracker,
		domain,
	):
		"""Validate location value."""		

		if RestaurantForm.check_if_location_exists(value):
			if RestaurantForm.check_location_validity(value) :
				# validation succeeded, set the value of the "location" slot to value
				return {"location": value}
			else:
				dispatcher.utter_template("utter_reselect_location", tracker)
				# validation failed, set this slot to None, meaning the
				# user will be asked for the slot again
				return {"location": None}
		else:
			dispatcher.utter_template("utter_ask_correct_location", tracker)
			return {"location": None}



	

class SendEmail(FormAction):
	""" custom form for email delivery"""

	def name(self):
		"""Unique identifier of the form"""
		return "send_email"
	

	def slot_mappings(self):
		"""A dictionary to map required slots to
		- an extracted entity
		- intent: value pairs
		- a whole message or a list of them, where a first 
									match will be picked"""

		return { "email_req": [self.from_intent(intent='affirm',
													value=True),
						self.from_intent(intent='deny',
													value=False)]}
	
	@staticmethod
	def required_slots(tracker):
		"""A list of required slots that the form has to fill"""
		if tracker.get_slot('email_req') == False:
			return []
		else:
			return ["email_req","email"]
	
	def submit(self,dispatcher,
        tracker,domain):
		email_req = tracker.get_slot('email_req')
		email = tracker.get_slot('email')
		response = tracker.get_slot('response')
		if email_req and email:
			# using thread as rasa server throws timeout exeception in 10 sec
			thread=Thread(target=SendEmail.send_mail,args=(response,email))
			thread.start()			
			dispatcher.utter_template("utter_sent_email",tracker)
		return[]
	
	@staticmethod
	def send_mail(response,email):
		requests.post("https://7635947d.ngrok.io/send-mail",json={"restaurants":str(response),"email":email})


