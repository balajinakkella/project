#pip install flask_mail.py

from flask import Flask
from flask.ext.mail import Mail, Message
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app =Flask(__name__)
mail=Mail(app)

app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'you@yourmail.com',
	MAIL_PASSWORD = '**********'
	)

mail=Mail(app)
@app.route("/")
def index():
	msg = Message('Hello',sender='you@yourmail.com',recipients=['sender@sendermail.com'])
	msg.body = "your message goes here...."
	mail.send(msg)
	return "Sent"

if __name__ == "__main__":
    app.run()
