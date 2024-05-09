from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from login.serializer import UserSerializer, SendEmailSerializer, VerifyOtpSerializer, UserProfileSerializer
from login.models import User
from rest_framework.generics import RetrieveAPIView, CreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from login.email_service import send_otp_via_email
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from Linktree.permissions import IsUserObjectPermission


class UserApi(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class UserRegistration(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserProfileApi(RetrieveAPIView):
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserObjectPermission]


class SendEmail(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        data = request.data
        serialized_data = SendEmailSerializer(data=data)
        msg = 'Something went wrong.'
        if serialized_data.is_valid():
            user = get_object_or_404(User, email=data.get('email'))
            otp = send_otp_via_email(user_email=data.get('email'))
            user.otp = otp
            user.save()
            msg = 'Your Account verification email is send to your email.'
        return Response({
            'message': msg
        })


class VerifyOtp(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request):
        data = request.data
        serialized_data = VerifyOtpSerializer(data=data)
        msg = 'Something went wrong.'
        if serialized_data.is_valid():
            user = get_object_or_404(User, email=data.get('email'))
            msg = 'You have entered wrong OTP.'
            if user.otp == data.get('otp'):
                user.is_verified = True
                user.save()
                msg = 'Your account is successfully verified.'
        return Response({
            'message': msg
        })
