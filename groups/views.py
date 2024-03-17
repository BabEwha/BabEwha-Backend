# from .models import Group, Participate
# from .serializers import GroupSerializer
# from rest_framework import viewsets
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# # from rest_framework.viewsets import ModelViewSet
# # from rest_framework.authentication import BasicAuthentication, SessionAuthentication
# # from .models import Group, Participate
# # from .serializers import GroupSerializer, ParticipateSerializer
# # from rest_framework.response import Response

from .models import Group
from .serializers import GroupSerializer
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from .permissions import IsOwnerOrReadOnly
from rest_framework.response import Response
from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from .models import Group, Participate
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import GroupSerializer
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q


class GroupViewSet(viewsets.ModelViewSet):

    authentication_classes = [BasicAuthentication, SessionAuthentication]
    serializer_class = GroupSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['place']
    ordering_fields = ['created_at', 'closing_time']

    def get_queryset(self):
        """
        이 view는 사용자가 Participate 테이블에 is_active==True로 존재하지 않는 경우에만 그룹을 반환합니다.
        """
        current_user = self.request.user
        active_participation_groups = Participate.objects.filter(
        user=current_user, 
        is_active=True
    ).values_list('group', flat=True)
        
        queryset = Group.objects.filter(~Q(id__in=active_participation_groups))
        return queryset
        
    @action(detail=False, methods=['get'], url_path='closing-soon')
    def closing_soon(self, request):
        """
        마감 시간이 현재로부터 10분 이내인 그룹을 반환
        """
        current_time = timezone.now()
        time_threshold = current_time + timedelta(minutes=10)
        groups_closing_soon = self.get_queryset().filter(closing_time__lte=time_threshold, closing_time__gte=current_time)

        page = self.paginate_queryset(groups_closing_soon)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        else:
            # page가 None일 경우 빈 리스트와 함께 Response 객체 반환
            return Response([])
        
    @action(detail=True, methods=['patch'], url_path='close-group')
    def close_group(self, request, pk=None):
        try:
            group = self.get_object()
            group.group_status = False
            group.save()
            return Response({'status': 'success', 'message': 'Group has been successfully closed.'}, status=status.HTTP_200_OK)
        except Group.DoesNotExist:
            return Response({'status': 'error', 'message': 'Group not found.'}, status=status.HTTP_404_NOT_FOUND)

    def get_serializer_context(self):
        context = super(GroupViewSet, self).get_serializer_context()
        context.update({
            'id': self.request.user.id  
        })
        return context
    



    # @action(detail=True, methods=['patch'], permission_classes=[IsAuthenticated])
    # def enter(self, request, pk=None):
    #     group = self.get_object()
    #     user = request.user
        
    #     # 이미 참여한 기록이 있는지 확인하고, 없다면 생성
    #     participation, created = Participate.objects.get_or_create(
    #         user=user,
    #         group=group,
    #         defaults={'status': True}
    #     )
        
    #     # 이미 참여 기록이 있지만 status가 False인 경우, True로 업데이트
    #     if not created and not participation.status:
    #         participation.status = True
    #         participation.save()
            
    #     return Response({'message': 'You have successfully create the group.'}, status=status.HTTP_200_OK)


    

