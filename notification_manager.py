from twilio.rest import Client
import smtplib

TWILIO_SID = "YOUR TWILIO ACCOUNT SID"
TWILIO_AUTH_TOKEN = "YOUR TWILIO AUTH TOKEN"
TWILIO_VIRTUAL_NUMBER = "YOUR TWILIO VIRTUAL NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR TWILIO VERIFIED NUMBER"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_emails(self, message, clients):
        print(f"All clinets: {clients}\nMessage: {message}")

        MY_EMAIL = "YOUR EMAIL"
        MY_PASSWORD = "YOUR PASSWORD"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)

            message = 'Subject: Flight deal\n\n' + message

            for client_email in clients:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=client_email,
                    msg=message.encode('utf-8')
                )


