from rest_framework import serializers
from stationapi.models import User,Incident,Feedback,IncidentStatus,CustomUser


class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)
    last_logged=serializers.CharField(read_only=True)

    class Meta:
        model=User
        fields=["id","username","name","location","phone","email_address","password","last_logged"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def validate(self, attrs):
        username = attrs.get('username')
        if username and CustomUser.objects.filter(username=username, user_type='User').exists():
            raise serializers.ValidationError({'username': 'Username already exists for a User.'})
        return attrs
    
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incident
        fields="__all__"  
        
class IncidentStatusSerializer(serializers.ModelSerializer):
    Incident=IncidentSerializer()
    class Meta:
        model=IncidentStatus
        fields="__all__" 
        
class FeedbackSerializer(serializers.ModelSerializer):
    incident=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    class Meta:
        model=Feedback
        fields="__all__"  