from django.db import models
from groups.models import Group
from order.models import Order

# Create your models here.


#payment/models.py
class Receipt(models.Model):
    class Meta :
        db_table = 'receipt'
    receipt_id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    receipt_image = models.ImageField(blank=True, upload_to="receipt/%Y/%m/%d")
    status = models.CharField(default='', max_length=100, null=False, blank=False)
    delivery_fee = models.IntegerField(null = True)
    discount_percent = models.IntegerField(null = True)
    discount_static = models.IntegerField(null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Payment(models.Model):
    class Meta :
        db_table = 'payment'
    payment_id = models.AutoField(primary_key=True)
    Receipt = models.ForeignKey(Receipt, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu = models.TextField(default='', null=False) 
    menu_price = models.IntegerField()
    status = models.CharField(default='', max_length=100, null=False, blank=False)