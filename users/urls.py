from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/',   views.SignUpView.as_view()),
    path('', include('rest_framework.urls')),
    path('<int:user_id>/profile', views.UserProfileView.as_view(), name="profile_view"),
]