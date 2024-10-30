from rest_framework.views import APIView
from account.services import UserAccoutService
from rest_framework.response import Response
from account.utils import generate_access_token
from rest_framework.permissions import AllowAny
from account.serializers import EmailLoginSerializer, EmailSignupSerializer, UserAccountSerializer


class EmailSignupView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = UserAccoutService.create(serializer.validated_data)
        data = UserAccountSerializer(account).data
        return Response(data={'data': data}, status=200)


class EmailLoginView(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = EmailLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = UserAccoutService.retrieve(serializer.validated_data)
        if not account:
            return Response({'error': 'Invalid Credentials'}, 400)
        access_token = generate_access_token(account)
        return Response(data={'data':access_token }, status=200)