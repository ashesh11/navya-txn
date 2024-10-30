import os
import jwt
import datetime
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

def generate_access_token(user):
    access_token_payload = {
        "user_id": user.id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=(int(os.getenv('ACCESS_TOKEN_VALIDITY_PERIOD_IN_MINUTES')) * 60))
    }

    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY
    )

    return {'access_token': access_token}