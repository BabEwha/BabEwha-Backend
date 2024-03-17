from rest_framework import serializers
from .models import Order, OrderDetail
from groups.models import Participate
from rest_framework.decorators import action
from rest_framework.response import Response



## create 위
# def analyze_image(image, order):
    #     url = 'http://external.api/analyze-image'
    #     files = {'image': image}
        
    #     response = requests.post(url, files=files)
    #     if response.status_code == 200:
    #         data = response.json()
    #         menu = data.get('menu')
    #         price = data.get('price')
            
    #         # OrderDetail 객체 생성
    #         if menu and price:
    #             OrderDetail.objects.create(order=order, menu=menu, price=price)
    #         else:
    #             # 적절한 예외 처리 또는 에러 로깅
    #             print("Failed to get menu and price from the external API response.")
    #     else:
    #         # 응답 실패 처리
    #         print("Failed to analyze the image. Status code:", response.status_code)
   
        # image = validated_data.get('order_image')
        # if image:
        #     self.analyze_image(image, self.instance)



class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_id', 'group', 'user', 'order_image', 'order_time']
        read_only_fields = ('order_id',) 

    def create(self, validated_data):
        group = validated_data.get('group')
        user = self.context['request'].user  # 요청으로부터 사용자 정보 가져오기
        order_status = 'recruiting'  # 초기 상태 설정

        # Group의 현재 인원 확인
        current_number_of_people = Participate.objects.filter(group=group, is_active=True).count()

        # Group 인원 수 조건 검사
        if current_number_of_people >= group.max_people:
            # 현재 인원수가 최대 인원수 이상이면 Participate 및 Order 생성 X
            raise serializers.ValidationError("This group has reached its maximum number of people.")
        elif current_number_of_people + 1 == group.max_people:
            # 현재 인원수 + 1이 최대 인원수와 같으면 group_status를 'ordered_all'로 변경
            group.group_status = False
            group.save()
            order_status = 'ordered_all'
        else:
            order_status = 'recruiting'  

        # Order 객체 생성
        order = Order.objects.create(**validated_data, order_status=order_status)
        # Participate 객체 생성
        Participate.objects.create(user=user, group=group, is_active=True, is_owner=False)
        return order
    
    

        order_details = OrderDetail.objects.filter(order__in=orders)
        serializer = OrderDetailSerializer(order_details, many=True)
        return Response(serializer.data)


class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderDetail
        fields = '__all__'

