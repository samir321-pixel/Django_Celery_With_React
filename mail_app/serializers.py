from rest_framework import serializers

from .models import User_mail


class User_Mail_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_mail
        fields = '__all__'
