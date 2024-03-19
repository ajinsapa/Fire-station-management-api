from django.contrib import admin
from stationapi.models import Station,CustomUser,Employee,Vehicle,Equipment,Incident,Team_assign,Feedback,Training,TrainingList

# Register your models here.


admin.site.register(CustomUser)
admin.site.register(Station)
admin.site.register(Employee)
admin.site.register(Vehicle)
admin.site.register(Equipment)
admin.site.register(Incident)
admin.site.register(Team_assign)
admin.site.register(TrainingList)