from django.db import models

# Create your models here.
import uuid

from django.urls import reverse

from django.contrib.auth.models import User,AbstractUser

from django.core.exceptions import ValidationError

import re

def VALID(value):

  x=re.match('^09\d{9}$',value)

  if x:
    return value
  else:
     raise ValidationError('the phone number is incorrect')

class User(AbstractUser):

  id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=True)

  phone=models.CharField(max_length=11,null=True,blank=True,validators=[VALID],help_text='example:09121112020')

  created_at=models.DateTimeField(auto_now=False, auto_now_add=True)

  updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)

  def __str__(self):
        return self.username

class myuser(User):
  def location_numbers(self):
        return len(location.objects.filter(user__username=self.username))
  class Meta:
    proxy=True
    

class location(models.Model):

    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)

    user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='UtoL')

    title=models.CharField(max_length=50)

    address=models.TextField(max_length=100)

    staff=models.BooleanField(default=True)

    created_at=models.DateTimeField(auto_now=False, auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.address


    def get_staff_location(self):
        return reverse("staff_location")
    
