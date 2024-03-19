from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator,MaxValueValidator
from datetime import datetime
from django.utils import timezone


# Create your models here.


class CustomUser(AbstractUser):
    user_type_choices=[
        ('Station', 'Station'),
        ('Employee' ,'Employee'),
        ('User','User')
    ]
    user_type=models.CharField(max_length=50,choices=user_type_choices,default='User')



class Station(CustomUser):
    name=models.CharField(max_length=100,unique=True)
    location=models.CharField(max_length=100)
    phone=models.CharField(max_length=100,unique=True)
    email_address=models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    
    
class Employee(CustomUser):
    name=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=100,unique=True)
    email_address=models.EmailField(unique=True)
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.name
   
    
class User(CustomUser):
    name=models.CharField(max_length=50,unique=True)
    phone=models.CharField(max_length=100,unique=True)
    email_address=models.EmailField(unique=True)
    location=models.CharField(max_length=100)
    last_logged=models.DateTimeField(auto_now_add=True,null=True)
    

    def __str__(self):
        return self.name
    
    def set_inactive(self):
        self.last_logged = timezone.now()
        self.save()
    
class Guest(models.Model):
    name=models.CharField(max_length=100)
    
    
class Equipment(models.Model):
    name=models.CharField(max_length=100)
    quantity=models.PositiveIntegerField()
    maintenance_record=models.CharField(max_length=100)
    expiration_date=models.DateField()
    is_available=models.BooleanField(default=True)
    
class Vehicle(models.Model):
    vehicle_type=models.CharField(max_length=100)
    plate_number=models.CharField(max_length=100)
    is_available=models.BooleanField(default=True)
    
    
class Incident(models.Model):
    date_time=models.DateTimeField()
    location=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    severity=models.CharField(max_length=100,null=True)
    description=models.CharField(max_length=100,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    
    
class IncidentStatus(models.Model):
    Incident=models.OneToOneField(Incident,on_delete=models.CASCADE,unique=True)
    options=[
        ('Alerted', 'Alerted'),
        ('Saved', 'Saved'),
        ('InProgress', 'In Progress'),
        ('Completed', 'Completed'),
        ('Closed', 'Closed')
    ]
    status=models.CharField(max_length=50,choices=options,default="Alerted")
        

class Team(models.Model):
    name = models.CharField(max_length=100)
    employees = models.ManyToManyField(Employee)
    is_available=models.BooleanField(default=True)


class Team_assign(models.Model):
    incident = models.OneToOneField(Incident, on_delete=models.CASCADE,unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    
    
class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    incident=models.ForeignKey(Incident,on_delete=models.CASCADE)
    # rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    comment=models.CharField(max_length=300)
    
    
class Certification(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date_of_completion = models.DateField()
    expiration_date = models.DateField(null=True, blank=True)
    employee = models.ForeignKey(Employee, related_name='certifications', on_delete=models.CASCADE)
    
class TrainingList(models.Model):
    name = models.CharField(max_length=100)
    video = models.FileField(upload_to='training_videos/')
    video_duration = models.DurationField()

class Training(models.Model):
    training_list = models.ForeignKey(TrainingList, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')

    
    



    