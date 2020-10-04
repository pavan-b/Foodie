
## happy path
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
* affirm
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "goa"}
    - form: restaurant_form
    - slot{"location": "goa"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Thai"}
    - form: restaurant_form
    - slot{"cuisine": "Thai"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "300 - 700"}
    - form: restaurant_form
    - slot{"avg_budget": "300 - 700"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "mumbai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "300 - 700"}
    - form: restaurant_form
    - slot{"avg_budget": "300 - 700"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "marathalli"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Bangalore"}
    - form: restaurant_form
    - slot{"location": "Bangalore"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "American"}
    - form: restaurant_form
    - slot{"cuisine": "American"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - form{"name": null}
    - slot{"requested_slot": null}
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "0 - 300"}
    - form: restaurant_form
    - slot{"avg_budget": "0 - 300"}
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Bangalore"}
    - form: restaurant_form
    - slot{"location": "Bangalore"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Thai"}
    - form: restaurant_form
    - slot{"cuisine": "Thai"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "300 - 700"}
    - form: restaurant_form
    - slot{"avg_budget": "300 - 700"}
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "tttttttttttttttttttttttttttt"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Vikarabad"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Finland"}
    - form: restaurant_form
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "hyderabad"}
    - form: restaurant_form
    - slot{"location": "hyderabad"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Mexican"}
    - form: restaurant_form
    - slot{"cuisine": "Mexican"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "300 - 700"}
    - form: restaurant_form
    - slot{"avg_budget": "300 - 700"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kochi"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Kochi"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Nasi And Mee in 66/6539, 2nd Floor, Narayanan Seva Sangam Building, Mullassery Canal Road, Shenoys, MG Road, Kochi has been rated 4.9. And the average price for two people here is: 1000 Rupees.\n Barbeque Nation in 6th Floor, Imperial Trade Centre, Mahatma Gandhi Road, Kacheripady, Kochi has been rated 4.9. And the average price for two people here is: 1500 Rupees.\n Mocha Art Cafe in 6/127, Opposite Jew Synagogue, Mattancherry, Kochi has been rated 4.8. And the average price for two people here is: 700 Rupees.\n Kochi Kitchen - Kochi Marriott Hotel in Kochi Marriott Hotel, Lulu International Shopping Mall, 34/1111 N. H. 47, Edappally, Kochi has been rated 4.7. And the average price for two people here is: 2000 Rupees.\n Paragon in F 82-83, Level 1, LuLu Mall, NH-17, Entrance Road, Edapally Junction, Edappally, Kochi has been rated 4.6. And the average price for two people here is: 900 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "test@gmail.com"}
    - form: send_email
    - slot{"email": "test@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Thai", "location": "Mumbai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Thai"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Palladium Social in Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.9. And the average price for two people here is: 1400 Rupees.\n Peco Peco in Shop 26, Linkway Estate, New Link Road, Near Shakti Motors, Malad West, Mumbai has been rated 4.9. And the average price for two people here is: 700 Rupees.\n Butterfly High in Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai has been rated 4.8. And the average price for two people here is: 1500 Rupees.\n Hitchki in Ground Floor, Viviana Mall, Eastern Express Highway, Near Jupiter Hospital, Majiwada, Thane West, Thane has been rated 4.8. And the average price for two people here is: 1600 Rupees.\n Colaba Social in 24, Ground Floor, Glen Rose Building, Behind Taj Mahal Palace, Apollo Bunder, Colaba, Mumbai has been rated 4.8. And the average price for two people here is: 1400 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "email.@gmail.com"}
    - form: send_email
    - slot{"email": "email.@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Visakhapatnam"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Visakhapatnam"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "North Indian"}
    - form: restaurant_form
    - slot{"cuisine": "North Indian"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "300 - 700"}
    - form: restaurant_form
    - slot{"avg_budget": "300 - 700"}
    - slot{"response": " Sri Sairam Parlour in Diamond Park, Railway New Colony Road, Dwaraka Nagar, Vizag has been rated 4.5. And the average price for two people here is: 300 Rupees.\n Alpha Hotel in 28-10-33/6, Jagdamba Commercial Complex, Chitralaya Cinema Hall, Jagadamba Junction, Vizag has been rated 4.3. And the average price for two people here is: 500 Rupees.\n Hotel Prabha Veg Restaurant in 58/1/406, Nad Kotha Road Junction, Visakhapatnam has been rated 4.3. And the average price for two people here is: 300 Rupees.\n Hotel V Parlour in Asilmetta Junction, Rama talkies Road, Dwaraka Nagar, Visakhapatnam has been rated 4.2. And the average price for two people here is: 500 Rupees.\n Raju's Kitchen in 53-32-1, HB Colony Road, Beside Allurisitharamaraju Statue, Seethammadhara, Vizag has been rated 4.2. And the average price for two people here is: 350 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "mumbai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "mexican"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "0 - 300"}
    - form: restaurant_form
    - slot{"avg_budget": "0 - 300"}
    - slot{"response": ""}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* deny
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "yryryryryry"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "Varanasi"}
    - form: restaurant_form
    - slot{"location": "Varanasi"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "North Indian"}
    - form: restaurant_form
    - slot{"cuisine": "North Indian"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Roma's Café Diner in 2nd Floor, Swastik Plaza, Lanka, Varanasi has been rated 4.8. And the average price for two people here is: 800 Rupees.\n Barbeque Nation in 3rd Floor, JHV Mall, The Mall Road, Varanasi Cantt, Nadesar, Varanasi has been rated 4.7. And the average price for two people here is: 1500 Rupees.\n UP- 65 in 3, Gurudham Road, Durgakund Road, Durgakund, Varanasi has been rated 4.6. And the average price for two people here is: 800 Rupees.\n Tadka - Ramada Plaza in Ramada Plaza JHV, The Mall, Cantonment, Nadesar, Varanasi has been rated 4.6. And the average price for two people here is: 1200 Rupees.\n The Big Tamaasha Cafe in Shop 60, LGF, Kuber Complex, Sigra, Varanasi has been rated 4.5. And the average price for two people here is: 1000 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: deny
    - form: send_email
    - slot{"email_req": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "North Indian"}
    - form: restaurant_form
    - slot{"cuisine": "North Indian"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "0 - 300"}
    - form: restaurant_form
    - slot{"avg_budget": "0 - 300"}
    - slot{"response": ""}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "hi@gmail.com"}
    - form: send_email
    - slot{"email": "hi@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Bangalore"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "Italian"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " AB's - Absolute Barbecues in 90/4, 3rd Floor, Outer Ring Road, Munnekollaly Village, Marathahalli, Bangalore has been rated 4.9. And the average price for two people here is: 1600 Rupees.\n Stories - The Brew Chapter in 348/1/2, Survey 62, 29th Main, 2nd Stage, Lake Road, BTM, Bangalore has been rated 4.9. And the average price for two people here is: 2000 Rupees.\n Biergarten in 4th B Cross, Koramangala 5th Block, Bangalore has been rated 4.9. And the average price for two people here is: 2600 Rupees.\n Byg Brewski Brewing Company in Behind MK Retail, Sarjapur Road, Bangalore has been rated 4.9. And the average price for two people here is: 1600 Rupees.\n The Black Pearl in 105, 1st A Cross Road, Jyothi Nivas College Road, Koramangala 5th Block, Bangalore has been rated 4.9. And the average price for two people here is: 1500 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: deny
    - form: send_email
    - slot{"email_req": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Raipur"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Raipur"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "American"}
    - form: restaurant_form
    - slot{"cuisine": "American"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "0 - 300"}
    - form: restaurant_form
    - slot{"avg_budget": "0 - 300"}
    - slot{"response": " Bajrang Restaurant in Near Aamanaka Railway Crossing, Amanaka, Raipur has been rated 4.1. And the average price for two people here is: 200 Rupees.\n Chai Sutta Bar in Infront Of Shiv Madir, Devendra Nagar, Raipur has been rated 3.9. And the average price for two people here is: 99 Rupees.\n World of Fries in 1, SLT Waterfront Building, Marine Drive, Telibandha Civil Lines, Raipur has been rated 3.7. And the average price for two people here is: 250 Rupees.\n World Of Fries in E 105, Main Road, Devendra Nagar, Raipur has been rated 3.7. And the average price for two people here is: 250 Rupees.\n English Veg Fast Food in Dropped Pin, Near Bangali Samiti Tatibandh, Shri Shanti Nath Nagar, Tatibandh, Raipur has been rated 3.5. And the average price for two people here is: 200 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: deny
    - form: send_email
    - slot{"email_req": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "hyderabad"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "hyderabad"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Paradise Biryani in Plot 22-23, Vinayaknagar, Gachibowli Main Road, Gachibowli, Hyderabad has been rated 4.9. And the average price for two people here is: 800 Rupees.\n Amnesia Sky Bar in 3rd Floor, Inorbit Mall, Mind Space Road, Hitech City, Hyderabad has been rated 4.9. And the average price for two people here is: 1500 Rupees.\n AB's - Absolute Barbecues in 8-2-618/10-11, 2nd Floor, Survey 129/70/283, Krishe Amethyst, Road 1, Banjara Hills, Hyderabad has been rated 4.9. And the average price for two people here is: 1500 Rupees.\n AB's - Absolute Barbecues in Second Floor, Apurupa Silpi, Indiranagar, Gachibowli, Hyderabad has been rated 4.9. And the average price for two people here is: 1200 Rupees.\n China Bistro in 1st Floor, Signature Towers, Opposite Botanical Garden, Kondapur, Hyderabad has been rated 4.9. And the average price for two people here is: 1600 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "yes@gmail.com"}
    - form: send_email
    - slot{"email": "yes@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "mumbai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Pepper & Pint in 2nd Floor, Horizon, Juhu Tara Road, Juhu, Mumbai has been rated 4.9. And the average price for two people here is: 1800 Rupees.\n Palladium Social in Level 3, Palladium Mall, Senapati Bapat Marg, Lower Parel, Mumbai has been rated 4.9. And the average price for two people here is: 1400 Rupees.\n Butterfly High in Unit 4, Ground Floor, Jet Airways, Godrej G Block, Near MCA, Bandra Kurla Complex, Mumbai has been rated 4.8. And the average price for two people here is: 1500 Rupees.\n Hitchki in 002, First International Financial Centre, G Block, Bandra Kurla Complex, Mumbai has been rated 4.8. And the average price for two people here is: 1600 Rupees.\n Hitchki in Ground Floor, Viviana Mall, Eastern Express Highway, Near Jupiter Hospital, Majiwada, Thane West, Thane has been rated 4.8. And the average price for two people here is: 1600 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "sdfsd@gmail.com"}
    - form: send_email
    - slot{"email": "sdfsd@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Gowhati"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: restaurant_search{"location": "goa"}
    - form: restaurant_form
    - slot{"location": "goa"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Mexican"}
    - form: restaurant_form
    - slot{"cuisine": "Mexican"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Cantare in 7/73 B, Cruz Waddo, Saligao, Near Calangute, Goa has been rated 4.0. And the average price for two people here is: 800 Rupees.\n The Station in 80 Belloy Nuvem , NH 17 Goa, Nuvem, Majorda, Goa has been rated 3.8. And the average price for two people here is: 800 Rupees.\n Arbor Brewing Company - Beer Garden & Eatery in The Archway, 1/9-A, Grand Morod, Saligao, Goa has been rated 3.8. And the average price for two people here is: 1200 Rupees.\n Zoori's Grill Restaurant in Poonam Resort Road, Dmello Vaddo, Anjuna, Goa, has been rated 3.6. And the average price for two people here is: 1000 Rupees.\n Harbour Cafe in The Crown Hotel, Lobby Level, Bairo Alto Dos Pilotos, Jose Falcao Road, Panaji, Goa has been rated 3.5. And the average price for two people here is: 1000 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "test@yahoo.com"}
    - form: send_email
    - slot{"email": "test@yahoo.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "mumbai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "italian"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Veranda in Hotel Executive Enclave, 331, Dr Ambedkar Road, Pali Hill, Bandra West has been rated 4.9. And the average price for two people here is: 2200 Rupees.\n London Taxi in 2nd Floor, Gabbana House, 15th Road, Opposite Toyota Showroom, Khar, Mumbai has been rated 4.9. And the average price for two people here is: 1800 Rupees.\n Ministry Of Dance in 7, Remi Commercio, Shah Industrial Road, New Link Road, Veera Desai Area, Mumbai has been rated 4.9. And the average price for two people here is: 1900 Rupees.\n Konkani Haus Restaurant & Bar in Rajnigandha Society 3, 4 & 5, Opposite Vandana Talkies, LBS Marg, Panch Pakhadi, Thane West, Thane has been rated 4.9. And the average price for two people here is: 1100 Rupees.\n Indiana Water's in 2nd Floor, Seawoods Grand Central Mall, Seawoods Station Road, Sector 40, Nerul, Navi Mumbai has been rated 4.9. And the average price for two people here is: 1200 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "email@gmail.com"}
    - form: send_email
    - slot{"email": "email@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Chennai"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "Thai"}
    - form: restaurant_form
    - slot{"cuisine": "Thai"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Mainland China in 1st Floor, 142, Phoenix Market City, Velachery, Chennai has been rated 4.7. And the average price for two people here is: 1800 Rupees.\n Nasi And Mee in 18/24, Yafa Towers, Khader Nawaz Khan Road, Thousand Lights West, Nungambakkam, Chennai has been rated 4.6. And the average price for two people here is: 1200 Rupees.\n Mamagoto in Shop 9, Oyster Building, Khader Nawaz Khan Road, Nungambakkam, Chennai has been rated 4.6. And the average price for two people here is: 2000 Rupees.\n Wok Monk in 117, 2nd Floor, Ravilla Towers, 3rd Avenue, W Block, Anna Nagar West, Chennai has been rated 4.6. And the average price for two people here is: 1200 Rupees.\n Soy Soi in 2/10, Gandhi Mandapam Road, Kotturpuram, Chennai has been rated 4.5. And the average price for two people here is: 1400 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: deny
    - form: send_email
    - slot{"email_req": false}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "cuisine"}
* form: restaurant_search{"cuisine": "chinese"}
    - form: restaurant_form
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "avg_budget"}
* form: restaurant_search{"avg_budget": "700 +"}
    - form: restaurant_form
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Veranda in Hotel Executive Enclave, 331, Dr Ambedkar Road, Pali Hill, Bandra West has been rated 4.9. And the average price for two people here is: 2200 Rupees.\n Ministry Of Dance in 7, Remi Commercio, Shah Industrial Road, New Link Road, Veera Desai Area, Mumbai has been rated 4.9. And the average price for two people here is: 1900 Rupees.\n London Taxi in 2nd Floor, Gabbana House, 15th Road, Opposite Toyota Showroom, Khar, Mumbai has been rated 4.9. And the average price for two people here is: 1800 Rupees.\n Konkani Haus Restaurant & Bar in Rajnigandha Society 3, 4 & 5, Opposite Vandana Talkies, LBS Marg, Panch Pakhadi, Thane West, Thane has been rated 4.9. And the average price for two people here is: 1100 Rupees.\n Pepper & Pint in 2nd Floor, Horizon, Juhu Tara Road, Juhu, Mumbai has been rated 4.9. And the average price for two people here is: 1800 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "email@gmail.com"}
    - form: send_email
    - slot{"email": "email@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye


## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai", "avg_budget": "700 +"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"avg_budget": "700 +"}
    - slot{"response": " Veranda in Hotel Executive Enclave, 331, Dr Ambedkar Road, Pali Hill, Bandra West has been rated 4.9. And the average price for two people here is: 2200 Rupees.\n Ministry Of Dance in 7, Remi Commercio, Shah Industrial Road, New Link Road, Veera Desai Area, Mumbai has been rated 4.9. And the average price for two people here is: 1900 Rupees.\n London Taxi in 2nd Floor, Gabbana House, 15th Road, Opposite Toyota Showroom, Khar, Mumbai has been rated 4.9. And the average price for two people here is: 1800 Rupees.\n Konkani Haus Restaurant & Bar in Rajnigandha Society 3, 4 & 5, Opposite Vandana Talkies, LBS Marg, Panch Pakhadi, Thane West, Thane has been rated 4.9. And the average price for two people here is: 1100 Rupees.\n Pepper & Pint in 2nd Floor, Horizon, Juhu Tara Road, Juhu, Mumbai has been rated 4.9. And the average price for two people here is: 1800 Rupees.\n"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - send_email
    - form{"name": "send_email"}
    - slot{"requested_slot": "email_req"}
* form: affirm
    - form: send_email
    - slot{"email_req": true}
    - slot{"requested_slot": "email"}
* form: email_address{"email": "email@gmail.com"}
    - form: send_email
    - slot{"email": "email@gmail.com"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_goodbye
