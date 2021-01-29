from twilio.rest import Client

client = Client("AC0b57db73de30c7a002c67af0b8c9713e",
                "7a0a36a632e761de7e9ab6245e7d7039")

# & GET all the message sent by your number

for msg in client.messages.list():
    print(msg.body)

# & Create a new message through twilio account
# msg = client.messages.create(
#     to="+918077869264",
#     from_="+15105925067",
#     body="Hello from Python!"
# )

# print(f"Created a new message: {msg.sid}")
