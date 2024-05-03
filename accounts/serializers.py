from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            #조건이라고 할수 있지
            "id",
            "email",
            "username",
            "password",
            "first_name",
            "last_name",
            "gender",
            "birthday"
        ]
