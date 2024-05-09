from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from theme.serializer import ThemeSerializer
from theme.models import Theme


class AdminThemeApi(ModelViewSet):
    serializer_class = ThemeSerializer
    queryset = Theme.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]