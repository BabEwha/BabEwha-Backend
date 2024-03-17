from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        fields = ['nickname', 'phone', 'bank_name', 'account_number', 'email', 'name']
    
    def get_email(self, obj):
        return obj.user.email

    def get_name(self, obj):
        return obj.user.name


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name']
        )
        Profile.objects.create(user=user, **profile_data)
        return user
      