from rest_framework import  serializers
from .models import UserInfo

class UserInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'
