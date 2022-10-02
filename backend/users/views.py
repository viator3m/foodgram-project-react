from djoser.views import UserViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import User
from .serializers import UsersSerializer


class UsersViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)


