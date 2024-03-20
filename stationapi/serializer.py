from rest_framework import serializers
from stationapi.models import Station,Employee,Equipment,Incident,Team_assign,Team,User,Vehicle,Feedback,Certification,TrainingList,IncidentStatus,CustomUser



class StationSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    password=serializers.CharField(write_only=True)

    class Meta:
        model=Station
        fields=["id","username","name","location","phone","email_address","password"]

    def create(self, validated_data):
        return Station.objects.create_user(**validated_data)
    
    def validate(self, attrs):
        username = attrs.get('username')
        if username and CustomUser.objects.filter(username=username, user_type='Station').exists():
            raise serializers.ValidationError({'username': 'Username already exists for a Station.'})
        return attrs
    
    
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employee
        fields=["id","name","phone","email_address","is_available"]
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","name","last_logged"]
        
class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipment
        fields="__all__"
        
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Incident
        fields="__all__"

class IncidentStatusSerializer(serializers.ModelSerializer):
    Incident=serializers.CharField(read_only=True)
    class Meta:
        model=IncidentStatus
        fields="__all__"
        
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model=Team
        fields="__all__"


class TeamViewSerializer(serializers.ModelSerializer):
    employees=serializers.SerializerMethodField()

    def get_employees(self, obj):
        return [employee.employee.name for employee in obj.employees.all()]
    
    class Meta:
        model=Team
        fields="__all__"

        
class AssignteamSerializer(serializers.ModelSerializer):
    incident=serializers.CharField(read_only=True)
    class Meta:
        model=Team_assign
        fields="__all__"

class AssignteamViewSerializer(serializers.ModelSerializer):
    incident=IncidentSerializer()
    team=TeamSerializer()
    class Meta:
        model=Team_assign
        fields="__all__"
        
        

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle
        fields="__all__"
        
        

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model=Feedback
        fields="__all__"
        

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = "__all__"
        
class TrainingListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingList
        fields = "__all__"