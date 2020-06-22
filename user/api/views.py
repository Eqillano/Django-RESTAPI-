from rest_framework.generics import (CreateAPIView,
                                    DestroyAPIView,
                                    ListAPIView,
                                    UpdateAPIView,
                                    RetrieveAPIView
                                    )
from .serializers import UserSerializer
from user.models import TestUser

''' классы для CRUD методов '''

class UserList(ListAPIView):
    serializer_class = UserSerializer
    queryset = TestUser.objects.all()


class UserDetail(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = TestUser.objects.all()
    lookup_field = 'id'



class UserCreate(CreateAPIView):
    serializer_class = UserSerializer


class UserDelete(DestroyAPIView):
    serializer_class = UserSerializer
    queryset = TestUser.objects.all()
    lookup_field = 'id'

class UserUpdate(UpdateAPIView):
    serializer_class = UserSerializer
    queryset = TestUser.objects.all()
    lookup_field = 'id'
