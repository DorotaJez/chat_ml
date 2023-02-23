from .models import CustomUserGroup
from django import forms
from ajax_select.fields import AutoCompleteSelectMultipleField

class GroupForm(forms.ModelForm):
    class Meta:
        model = CustomUserGroup
        fields = ['custom_group_name','users',]
        
    users = AutoCompleteSelectMultipleField('users', required=True, help_text=None)
