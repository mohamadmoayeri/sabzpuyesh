from django.urls import path,include

from .views import *

urlpatterns = [
    path('staff_location',staff_location ,name='staff_location'),
    path('user_serial',user_serial,name='user_serial'),
    path('staff_lists',staff_lists.as_view(),name='staff_lists'),
    path('write_address',write_address,name='write_address'),
    
]
