import jwt

from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import exceptions
from rest_framework.authentication import BaseAuthentication

User = get_user_model()


class AccountJWTAuthentication(BaseAuthentication):
    """
    Custom authentication class for handling JWT-based authentication.
    
    This class overrides the `authenticate` method, which extracts the 
    authorization token from the request header and verifies it. If the 
    token is valid and the user exists, the authenticated user instance 
    is returned; otherwise, appropriate exceptions are raised.
    """

    def authenticate(self, request):
        """
        Authenticate the request using JWT tokens.

        This function extracts the JWT token from the request's authorization 
        header and validates it. The token is decoded using the application's 
        SECRET_KEY and a specified algorithm. The decoded token provides user 
        information, specifically the user ID, which is used to retrieve the 
        user from the database. If authentication succeeds, a tuple of the 
        authenticated user and `None` (for session) is returned.

        Parameters:
        ----------
        request : HttpRequest
            The incoming HTTP request to be authenticated.

        Returns:
        -------
        tuple : (User instance, None)
            If the token is valid and the user exists, returns the authenticated 
            User instance and None.

        Raises:
        ------
        PermissionDenied:
            Raised when there is no authorization header or if the token is invalid.
        ValidationError:
            Raised when the token signature is invalid.
        NotFound:
            Raised when the user corresponding to the token is not found.
        """
        
        authorization_header = request.headers.get('Authorization')

        if authorization_header is None:
            raise exceptions.PermissionDenied({'error': 'No authorization header'})
        
        try:
            access_token = authorization_header.split(" ")[1] if len(authorization_header.split(" ")) > 1 else None
            if not access_token:
                raise exceptions.PermissionDenied({'error': 'Invalid token'})
            
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms='HS256'
            )
        
        except jwt.exceptions.ExpiredSignatureError:
            raise exceptions.PermissionDenied({'error': 'Expired Signature'})
        
        except Exception as e:
            raise exceptions.ValidationError({'error': 'Invalid Signature'})

        
        user = User.objects.filter(id=payload['user_id']).first()

        if user is None:
            raise exceptions.NotFound({'error': 'User not found'})
        
        if not user.is_active:
            raise exceptions.PermissionDenied({'error': 'User is inactive'})

        return(user, None)