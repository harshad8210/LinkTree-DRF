from rest_framework.permissions import IsAuthenticated, IsAdminUser
from Linktree.permissions import IsObjectOwnerPermission
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication
from links.serializer import LinkSerializer, UserLinkSerializer
from links.models import Link, UserLink
from rest_framework.response import Response


class AdminLinkApi(ModelViewSet):
    """
    Admin link APIs(CRUD)
        - To add, update, create, and delete link platform.
        - Only Admin user has permission
    """
    serializer_class = LinkSerializer
    queryset = Link.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]


class LinkApi(ListCreateAPIView):
    """
    Link APIs
        - User can get they link and create new links
    """
    serializer_class = UserLinkSerializer
    queryset = UserLink.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user_links = UserLink.objects.filter(user=request.user)
        res_data = self.serializer_class(user_links, many=True)
        return Response(res_data.data)


class UpdateDeleteLinkApi(RetrieveUpdateDestroyAPIView):
    """
    Link APIs(Retrieve, Update and Delete)
        - User can get, update and delete they link
    """
    serializer_class = UserLinkSerializer
    queryset = UserLink.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsObjectOwnerPermission]
