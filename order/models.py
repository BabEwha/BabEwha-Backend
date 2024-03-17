from django.db import models
from users.models import User
from groups.models import Group



class Order(models.Model):
    class Meta :
        db_table = 'order'
    order_id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 완료된 주문인지 (배달 도착 후 20분 뒤)
    is_order_active = models.BooleanField(default = True)
    # 주문을 하면 -> current number 추가하고
    # 만약 추가했을 때 max 넘으면 is_order_active를 False로 
    order_image = models.ImageField(null=True, blank=True, upload_to="order/%Y/%m/%d")
    order_time = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=100)


class OrderDetail(models.Model):
    class Meta :
        db_table = 'orderdetail'
    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    menu = models.TextField() 
    price = models.IntegerField()
  