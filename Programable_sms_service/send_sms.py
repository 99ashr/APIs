from twilio.rest import Client

account_sid = 'AC0b57db73de30c7a002c67af0b8c9713e'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGe4a4e6819ada8259bf7538bec6b77f28',
    body='I love you Shrankhla',
    to='+919001079493'
)

print(message.sid)
