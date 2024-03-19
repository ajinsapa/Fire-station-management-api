from django.urls import path
from stationapi import views
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("employees",views.EmployeeView,basename="employees")
router.register("equipments",views.EquipmentView,basename="equipments")
router.register("incidents",views.IncidentView,basename="incidents")
router.register("team",views.TeamCreateView,basename="team-create")
router.register("users",views.UserView,basename="users-list")
router.register("vehicle",views.VehicleView,basename="vehicles-list")
router.register("certificate",views.CertificationViewSet,basename="certificate")
router.register("trainings",views.TrainingListViewSet,basename="trainings")
router.register("incidentstatus",views.IncidentStatusView,basename="incidentstatus")


urlpatterns = [
    path("register/",views.StationCreateView.as_view(),name="signin"),
    path("token/",ObtainAuthToken.as_view(),name="token"),
    path("trainingstatus/",views.StationCompletedStatusView.as_view(),name="trainingstatus"),
    # path("logout/",views.sign_out,name="logout"),

] +router.urls