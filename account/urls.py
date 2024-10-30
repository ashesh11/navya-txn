from django.urls import path
from account.views import EmailSignupView

urlpatterns = [
    path('signup/email/', EmailSignupView.as_view(), name='email-signup')
]