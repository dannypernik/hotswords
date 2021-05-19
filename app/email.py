from threading import Thread
from app import app
from flask import render_template
from mailjet_rest import Client

def send_inquiry_email(user, message):
    api_key = app.config['MAILJET_KEY']
    api_secret = app.config['MAILJET_SECRET']
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
      'Messages': [
        {
          "From": {
            "Email": app.config['ADMINS'][0],
            "Name": "Hotswords.com"
          },
          "To": [
            {
              "Email": app.config['ADMINS'][0],
            }
          ],
          "Subject": "Contact Form Submission: " + user.first_name,
          "TextPart": render_template('email/inquiry-form.txt',
                                   user=user, message=message),
        }
      ]
    }

    result = mailjet.send.create(data=data)
    print(result.status_code)
    print(result.json())
