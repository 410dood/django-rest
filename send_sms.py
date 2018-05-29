from twilio.rest import Client;

def load_twilio_config():
    TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
    TWILIO_ACCOUNT_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')


    if not all([TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_AUTH_TOKEN]):
        logger.error(NOT_CONFIGURED_MESSAGE)
        raise MiddlewareNotUsed

    return (TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_AUTH_TOKEN)

client = Client(TWILIO_ACCOUNT_SID, TWILIO_ACCOUNT_AUTH_TOKEN)

message = client.messages.create(
    to="+17193298921", 
    from_="+17193236514",
    body="Hello :)")

print(message.sid)