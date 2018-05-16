from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .serializers import UserSerializer


User = get_user_model()


class RegistrationAPI(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    queryset = User.objects.all()
