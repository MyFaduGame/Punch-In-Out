from rest_framework import serializers
from punchinout.models import timein,User,timeout

# class timeinserializer(serializers.Serializer):
#     userid = serializers.CharField(max_length = 49)
#     date = serializers.DateField()
#     timein = serializers.TimeField()

#     class Meta:
#         table=timein

class timeinserializer(serializers.ModelSerializer):
    class Meta:
        model=timein
        fields=['userid','dateuser','timestampin']
    
class timeoutserializer(serializers.ModelSerializer):

    class Meta:
        model=timeout
        fields=['userid','dateuser','timestampout']