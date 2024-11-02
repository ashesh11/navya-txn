import os
import jwt
import datetime
from django.conf import settings
from dotenv import load_dotenv

load_dotenv()

def generate_access_token(user):
    """
    Generates a JWT access token for the specified user.

    This function creates a JWT token payload with the user ID and 
    timestamps for issuance and expiration. The expiration time is 
    calculated based on a configurable validity period (in minutes) 
    provided in the environment variables. The token is encoded using 
    the application's SECRET_KEY.

    Parameters:
    ----------
    user : User instance
        The user for whom the access token is generated.

    Returns:
    -------
    dict : { "access_token": str }
        A dictionary containing the generated JWT access token as a 
        string in the format: {"access_token": <encoded_token>}.
    """
    
    access_token_payload = {
        "user_id": user.id,
        "iat": datetime.datetime.utcnow(),
        "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=(int(os.getenv('ACCESS_TOKEN_VALIDITY_PERIOD_IN_MINUTES')) * 60))
    }

    access_token = jwt.encode(
        access_token_payload, settings.SECRET_KEY
    )

    return {'access_token': access_token}