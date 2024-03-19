from django.shortcuts import render
from stationapi.models import User,Incident,Feedback,IncidentStatus
from userapi.serializer import UserSerializer,IncidentSerializer,FeedbackSerializer,IncidentStatusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions
from django.contrib.auth import logout
from rest_framework import status





# Create your views here.


class UserCreateView(APIView):
    def post(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_type="User")
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class IncidentView(ViewSet):

    def create(self,request,*args,**kwargs):
        serializer=IncidentSerializer(data=request.data)
        user_obj=request.user.user
        if serializer.is_valid():
            serializer.save(user=user_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def list(self,request,*args,**kwargs):
        user_obj=request.user.user
        qs=IncidentStatus.objects.filter(Incident__user=user_obj)
        serializer=IncidentStatusSerializer(qs,many=True)
        return Response(data=serializer.data)
        

    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]      
    @action(methods=["post"],detail=True)
    def feedback_add(self,request,*args,**kwargs):
        serializer=FeedbackSerializer(data=request.data)
        user_obj=request.user.user
        incident_id=kwargs.get("pk")
        incident_obj=Incident.objects.get(id=incident_id)
        if serializer.is_valid():
            serializer.save(incident=incident_obj,user=user_obj)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]         
    @action(methods=["get"],detail=True)   
    def incident_status(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        incident_obj=Incident.objects.get(id=id)
        qs=IncidentStatus.objects.filter(Incident=incident_obj)
        serializer=IncidentStatusSerializer(qs,many=True)
        return Response(data=serializer.data)
        
# def sign_out(request):
#     logout(request)
#     user=request.user.user
#     print(user)
#     if user.is_authenticated:
#         user.set_inactive()
#     return render("signin")