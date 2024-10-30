from account.models import UserAccount


class UserAccoutService:
    @staticmethod
    def create(data):
        account = UserAccount.objects.create_user(
            name=data['name'],
            email=data['email'],
            password=data['password']
        )
        return account