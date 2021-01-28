from twilio.rest import Client

client = Client("AC0b57db73de30c7a002c67af0b8c9713e",
                "7a0a36a632e761de7e9ab6245e7d7039")

for msg in client.messages.list():
    print(msg.body)
