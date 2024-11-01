from account.models import UserAccount
from django.contrib.auth import authenticate


class UserAccoutService:
    @staticmethod
    def create(data):
        account = UserAccount.objects.create_user(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        return account
    
    @staticmethod
    def retrieve(data):
        account = authenticate(email=data['email'], password=data['password'])
        return account