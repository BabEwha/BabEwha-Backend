from django import forms
from .models import Group

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ['title', 'owner', 'body', 'place', 'detail_place' 'group_image', 'link', 'closing_time', 'max_people']
