from twilio.rest import TwilioRestClient

# Your Account SID from twilio.com/console
account_sid = "AC97630bac4ef277687bacebe738be2be4"
# Your Auth Token from twilio.com/console
auth_token  = "f6b829af73d8fff2ed995b8ba0*****" #auth_token incomplete

client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    to="+919740604155", 
    from_="+12177335021",
    body="Hello from Python!")

print(message.sid)
