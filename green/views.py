from django.shortcuts import render

# Create your views here.

from .models import location,myuser


from rest_framework.response  import Response

from rest_framework import status

from rest_framework.decorators import api_view

from rest_framework.generics import ListAPIView

from .serializers import user_serialize,staff_serialize,Address_Serializer

from django.http import HttpResponse

from django.db.models.signals import pre_save

from django.dispatch import  receiver
@receiver(pre_save,sender=location)
def send_notif(sender,**kwargs):

    print('adress is created')












def staff_location(request):

        l=[]
        adr=location.objects.filter(staff=True)

        for i in adr:
            l.append({'title':i.title,
                'adresss':i.address,
            
            })

        return HttpResponse(l)
        
    




@api_view(['GET'])
def user_serial(request):
    try:
      u=myuser.objects.all()

      s=user_serialize(u,many=True)

      data=s.data

      return Response({'data':data},status=status.HTTP_200_OK)
      
    except:

      return Response({'status':"internal_server_error"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class staff_lists(ListAPIView):
  queryset=myuser.objects.filter(is_staff=True)
  serializer_class=staff_serialize
  def get_queryset(self):
    qs=super().get_queryset()
    l=[]
    q=self.request.query_params
    
    if "location_numbers__gte" in q:
        for i in qs:

            if len(location.objects.filter(user__username=i.username)) >= int(q["location_numbers__gte"]):

                l.append(i.username)
        return qs.filter(username__in=l)
    elif "location_numbers__lte" in q:
        for i in qs:

            if len(location.objects.filter(user__username=i.username)) <= int(q["location_numbers__lte"]):

                l.append(i.username)
        return qs.filter(username__in=l)

    else:

            return qs

            



  
 

  
 
@api_view(['POST'])
def write_address(request):
    data=request.data

    ser =Address_Serializer(data=data,context={'request':request})
    print(ser)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else:
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)



