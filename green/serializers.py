from rest_framework import serializers

from .models import location,myuser

from django.utils import timezone


class user_serialize(serializers.ModelSerializer):

    class Meta:

        model=myuser

        fields=['first_name','last_name']


class staff_serialize(serializers.ModelSerializer):


    class Meta:

        model=myuser

        fields=['first_name','last_name',"location_numbers"]


    
class Address_Serializer(serializers.ModelSerializer):
    user_id=serializers.CharField(required=True)
    class Meta:
        model = location
        fields = '__all__'
        read_only_fields = ("id","user","created_at", "updated_at","staff")

    
   

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.user=myuser.objects.get(id=validated_data['user_id'])

        obj.created_at = timezone.now()
        r=self.context.get('request')
        u=r.user
        print(r)
        obj.staff=myuser.objects.get(username=u).is_staff
        obj.save()
        return obj

    def update(self, instance, validated_data):
        old_created_at = instance.created_at

        obj = super().update(instance, validated_data)
        obj.created_at = old_created_at
        obj.updated_at = timezone.now()
        obj.save()
        return obj


