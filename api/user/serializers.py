from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("id", "username", "email", "password", "is_staff")
        read_only_fields = ("id", "is_staff")
        extra_kwargs = {"password": {"write_only": True, "min_length": 5}}

    def create(self, validated_data):
        return get_user_model().objects.create_user(**validated_data)


class UserActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ("last_request", "last_login")
