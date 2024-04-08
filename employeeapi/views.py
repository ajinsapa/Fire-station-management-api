from django.shortcuts import render
from employeeapi.serializer import EmployeeSerializer,VehicleSerializer,EquipmentSerializer,TrainingSerializer,TrainingListSerializer,TrainingViewSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from stationapi.models import Vehicle,Team_assign,Team,Equipment,Training,TrainingList
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import permissions
from django.contrib.auth import logout
from rest_framework.decorators import action
from rest_framework import status
from django.contrib import messages




# Create your views here.


class EmployeeCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_type="Employee")
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_404_NOT_FOUND)
        
class EquipmentView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=EquipmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_available=True)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
    
    def list(self,request,*args,**kwargs):
        qs=Equipment.objects.all()
        serializer=EquipmentSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Equipment.objects.get(id=id)
        serializer=EquipmentSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance = Equipment.objects.get(id=id)
            instance.delete()
            return Response({"msg": "Equipment removed"})
        except Equipment.DoesNotExist:
            return Response({"msg": "Equipment not found"}, status=status.HTTP_404_NOT_FOUND)
        
        
class VehicleView(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def create(self,request,*args,**kwargs):
        serializer=VehicleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(is_available=True)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

    def list(self,request,*args,**kwargs):
        qs=Vehicle.objects.all()
        serializer=VehicleSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Vehicle.objects.get(id=id)
        serializer=VehicleSerializer(qs)
        return Response(data=serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        try:
            instance = Vehicle.objects.get(id=id)
            instance.delete()
            return Response({"msg": "Vehicle removed"})
        except Vehicle.DoesNotExist:
            return Response({"msg": "Vehicle not found"}, status=status.HTTP_404_NOT_FOUND)


    @action(methods=['post'], detail=True)
    def make_available(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        vehicle = Vehicle.objects.get(id=id)
        vehicle.is_available="True"
        vehicle.save()
        return response("vehicle made available")



    @action(methods=['post'], detail=True)
    def make_unavailable(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        vehicle = Vehicle.objects.get(id=id)
        vehicle.is_available="False"
        vehicle.save()
        return response("vehicle made unavailable")



class TrainingListViewSet(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    
    def list(self,request,*args,**kwargs):
        qs=TrainingList.objects.all()
        serializer=TrainingListSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=TrainingList.objects.get(id=id)
        serializer=TrainingListSerializer(qs)
        return Response(data=serializer.data)
    

    @action(methods=['post'], detail=True)
    def create_training(self,request,*args,**kwargs):
        employee=request.user.employee
        id = kwargs.get("pk")
        training = TrainingList.objects.get(id=id)
        serializer=TrainingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(employee=employee,training_list=training)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


        
class TrainingViewSet(ViewSet):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

        
    def list(self,request,*args,**kwargs):
        employee=request.user.employee
        qs=Training.objects.filter(employee=employee)
        serializer=TrainingViewSerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        qs=Training.objects.get(id=id)
        serializer=TrainingViewSerializer(qs)
        return Response(data=serializer.data)
        

    @action(methods=['post'], detail=True)
    def mark_completed(self, request, *args, **kwargs):
        employee = request.user.employee
        id = kwargs.get("pk")
        try:
            training = Training.objects.get(id=id)
        except Training.DoesNotExist:
            return Response({'error': 'Training not found'}, status=404)
        training.status = 'Completed'
        training.save()
        return Response({'status': 'Training marked as completed'})
    
    
    @action(methods=['get'], detail=False)
    def completion_percentage(self, request):
        user = request.user.employee
        total_trainings = TrainingList.objects.count()
        completed_trainings = Training.objects.filter(employee=user, status='Completed').count()
        if total_trainings > 0:
            completion_percentage = (completed_trainings / total_trainings) * 100
        else:
            completion_percentage = 0 
        return Response({'completion_percentage': completion_percentage})
        
        
# def sign_out(request):
#     logout(request)
    # user = request.user.employee
    # if user.is_authenticated:
    #     user.set_inactive()
    #     messages.info(request, "You have been successfully logged out.")
    # return render("signin")
    
    
    