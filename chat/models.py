from django.db import models
from django.contrib.auth.models import User

class CustomUserGroup(models.Model):
    custom_group_name = models.CharField(max_length=50,unique=True)
    users= models.ManyToManyField(User)

    class Meta:
        verbose_name_plural = 'Custom Groups'
        ordering = ['custom_group_name']

    def __unicode__(self):
        return self.custom_group_name
    
    def __repr__(self):
        return self.custom_group_name

    def __str__(self):
        return self.custom_group_name
    
users_list = []