from django.db import IntegrityError
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.exceptions import ValidationError

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=254)
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        try:
            user = User.objects.create_user(
                email=validated_data['email'],
                username=validated_data['email'],
                password=validated_data['password'],
                is_active=False
            )

            return user
        except IntegrityError:
            raise ValidationError('User with this email already exists')

    class Meta:
        fields = (
            'email', 'id', 'password',)
        model = User
        ref_name = 'CustomUserSerializer'
