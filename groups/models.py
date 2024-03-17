from django.db import models
from users.models import User

class Group(models.Model):
    class Meta :
        db_table = 'group'
    group_id = models.AutoField(primary_key=True)
    title = models.CharField(default='', max_length=100, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='', null=False, blank=False)
    place = models.CharField(max_length=20)
    detail_place = models.CharField(max_length=100)
    group_image = models.ImageField(blank=True, upload_to="groups/%Y/%m/%d")
    link = models.URLField("Site URL")
    created_at = models.DateTimeField(auto_now_add=True)
    closing_time = models.DateTimeField()
    max_people = models.IntegerField() 
    group_status = models.BooleanField(default = True) # True: 모집중 / False: X
    
class Participate(models.Model):
    class Meta:
        db_table = 'participate'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    is_owner = models.BooleanField(default=False) 
    is_active = models.BooleanField(default=True) 