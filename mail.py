from flask_mail import Mail, Message
from flask import Flask
from flask import request

app = Flask(__name__)
app.config.update(
	# DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'email@gmail.com',
	MAIL_PASSWORD = 'password'
	)
mail = Mail(app)

@app.route('/send-mail',methods=[ 'POST'])
def send_mail():
    print(request.method)
    if request.method == 'POST':
        r=request.json
        print(str(r))
        try:
            msg = Message("Restaurant details!",
            sender="email@gmail.com",
            recipients=[str(r['email'])])
            msg.body = str(r['restaurants'])
            mail.send(msg)
            return 'Mail sent!'
        except Exception as e:
            return(str(e))
    

if __name__ == '__main__':
   app.run()