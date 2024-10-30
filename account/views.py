from rest_framework.views import APIView
from account.services import UserAccoutService
from account.serializers import EmailLoginSerializer, EmailSignupSerializer, UserAccountSerializer
from rest_framework.response import Response

class EmailSignupView(APIView):
    def post(self, request):
        serializer = EmailSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = UserAccoutService.create(serializer.validated_data)
        data = UserAccountSerializer(account).data
        return Response(data={'data': data}, status=200)

class EmailLoginView(APIView):
    def post(self, request):
        pass