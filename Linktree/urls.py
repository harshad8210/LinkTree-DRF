from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from login.views import UserApi, SendEmail, VerifyOtp, UserProfileApi, UserRegistration
from socials.views import SocialsApi, AdminSocialsApi, RetrieveUpdateDestroySocialsApi
from links.views import AdminLinkApi, LinkApi, UpdateDeleteLinkApi
from theme.views import AdminThemeApi

router = DefaultRouter()
router.register('user', UserApi, basename='user')
router.register('socialsad', AdminSocialsApi, basename='admin socials')
router.register('linkadmin', AdminLinkApi, basename='admin links')
router.register('themeadmin', AdminThemeApi, basename='admin theme')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registration/', UserRegistration.as_view(), name='registration'),
    path('apitoken/', TokenObtainPairView.as_view(), name='get_token'),
    path('refreshtoken/', TokenRefreshView.as_view(), name='refresh_token'),
    path('sendemail/', SendEmail.as_view(), name='verification mail'),
    path('verifyemail/', VerifyOtp.as_view(), name='verify OTP'),
    path('socials/', SocialsApi.as_view(), name='socials'),
    path('socials/<int:pk>/', RetrieveUpdateDestroySocialsApi.as_view(), name='socials_retrieve_delete'),
    path('links/', LinkApi.as_view(), name='links'),
    path('profile/<int:pk>/', UserProfileApi.as_view(), name='User_profile'),
    path('links/<int:pk>/', UpdateDeleteLinkApi.as_view(), name='links updates'),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('social-auth/', include('drf_social_oauth2.urls', namespace='drf')),
    path('', include(router.urls)),
]

