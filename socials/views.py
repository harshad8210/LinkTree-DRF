from rest_framework.permissions import IsAuthenticated, IsAdminUser
from Linktree.permissions import IsObjectOwnerPermission
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from socials.serializer import SocialsSerializer, UserSocialsSerializer
from socials.models import SocialIcons, UserSocials
from rest_framework.response import Response


class AdminSocialsApi(ModelViewSet):
    serializer_class = SocialsSerializer
    queryset = SocialIcons.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class SocialsApi(ListCreateAPIView):
    serializer_class = UserSocialsSerializer
    queryset = UserSocials.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        social_profile = UserSocials.objects.filter(user=request.user)
        res_data = self.serializer_class(social_profile, many=True)
        return Response(res_data.data)


class RetrieveUpdateDestroySocialsApi(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSocialsSerializer
    queryset = UserSocials.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsObjectOwnerPermission]