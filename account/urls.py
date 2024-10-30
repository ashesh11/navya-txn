from django.urls import path
from account.views import EmailSignupView, EmailLoginView

urlpatterns = [
    path('signup/email/', EmailSignupView.as_view(), name='email-signup'),
    path('login/email/', EmailLoginView.as_view(), name='email-login')
]