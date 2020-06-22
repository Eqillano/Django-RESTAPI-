from rest_framework import serializers

from user.models import TestUser

""" сериализуем сущность в json """

class UserSerializer(serializers.ModelSerializer):
    class Meta:
          model = TestUser
          fields = ['id','username']


    def validate_username(self,value):
        qs = TestUser.objects.filter(username_iexact=value)
        if qs.exists():
           raise serializer.ValidationError('Имя не должно совпадать')
