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
            "Email": app.config['MAIL_USERNAME'],
            "Name": "Hotswords"
          },
          "To": [
            {
              "Email": app.config['ADMINS'][0],
            }
          ],
          "ReplyTo": {
                "Email": user.email,
          },
          "Subject": "Hotswords: Message from " + user.first_name,
          "TextPart": render_template('email/inquiry-form.txt',
                                   user=user, message=message),
        }
      ]
    }

    result = mailjet.send.create(data=data)

    if result.status_code is 200:
        send_confirmation_email(user, message)
        print("Confirmation email sent to " + user.email)
    else:
        print("Contact email failed with code " + result.status_code)
    print(result.json())


def send_confirmation_email(user, message):
    api_key = app.config['MAILJET_KEY']
    api_secret = app.config['MAILJET_SECRET']
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')

    data = {
        'Messages': [
            {
                "From": {
                    "Email": app.config['MAIL_USERNAME'],
                    "Name": "Hotswords"
                },
                "To": [
                    {
                    "Email": user.email
                    }
                ],
                "Subject": "Your message has been received",
                "TextPart": render_template('email/confirmation.txt',
                                         user=user, message=message),
                "HTMLPart": render_template('email/confirmation.html',
                                         user=user, message=message)
            }
        ]
    }

    result = mailjet.send.create(data=data)
    if result.status_code is 200:
        print(result.json())
    else:
        print("Confirmation email failed to send with code " + result.status_code, result.reason)
