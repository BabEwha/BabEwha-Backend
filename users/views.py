

# Create your views here.




# from django.shortcuts import get_object_or_404
# from .serializers import *
# from .models import User
# from rest_framework import generics
# from rest_framework.response import Response

# # 회원가입
# class SignUpView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserRegistrationSerializer

# # Profile 
# class UserProfileView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserProfileSerializer
#     lookup_field = 'user_id'  # Assuming the URL pattern captures this as <int:id> or similar


# users/views.py

from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import User, Profile
from .serializers import UserSerializer, ProfileSerializer

class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user = get_object_or_404(User, pk=user_id)
        profile = get_object_or_404(Profile, user=user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)
