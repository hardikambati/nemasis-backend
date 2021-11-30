from rest_framework import serializers
from .models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model = UserProfile
        fields = (
            'username', 'email', 'is_superuser', 'is_staff',
            'is_active', 'date_joined', 'address'
        )


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        min_length=1, write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = (
            'username', 'email', 'password', 'address'
        )

    def create(self, validated_data):
        return UserProfile.objects.create_user(**validated_data)