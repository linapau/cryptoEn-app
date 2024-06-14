from rest_framework import serializers
from data.models import UserModel

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['userID', 'username', 'password', 'email', 'encryptionKey']