from rest_framework import serializers
from .models import Group, Participate
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

class GroupSerializer(serializers.ModelSerializer):
    current_number_of_people = serializers.SerializerMethodField()

    class Meta:
        model = Group
        fields = ['group_id', 'title', 'body', 'place', 'detail_place','group_image', 'link','created_at', 'closing_time', 'max_people', 'current_number_of_people', 'group_status']

        read_only_fields = ['owner', 'created_at','current_number_of_people','group_status']
        
    
    def get_current_number_of_people(self, obj):
        return Participate.objects.filter(group=obj).count()

    def create(self, validated_data):
        user = self.context['request'].user

        # is_active == True인 Participate가 있는지 확인
        if Participate.objects.filter(user=user, is_active=True).exists():
            raise ValidationError('Active participation already exists.')

        # 이제 Group 생성 로직
        group = Group.objects.create(**validated_data, owner=user)
        Participate.objects.create(user=user, group=group, is_owner=True, is_active=True)
        
        return group
    




    # 마감시간, 마감인원에 따라 group status를 비활성화하는 함수 필요
    # 마감인원은 order에서 해도 될듯?


   # is_user_participating = serializers.SerializerMethodField('get_is_user_participating')
    
    # def get_group_status(self, obj): # 활성/비활성화
    #     current_time = timezone.now()
    #     if obj.closing_time < current_time or self.get_current_number_of_people(obj) >= obj.max_people:
    #         return False
    #     return True

     # def get_is_user_participating(self, obj):
    #     user = self.context.get('request').user
    #     return Participate.objects.filter(group=obj, user=user).exists()