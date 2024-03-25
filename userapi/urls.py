from django.urls import path
from userapi import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import ObtainAuthToken


router=DefaultRouter()
router.register("incident",views.IncidentView,basename="incident")
router.register("guestincident",views.GuestIncidentView,basename="incident")




urlpatterns = [
    path("register/",views.UserCreateView.as_view(),name="signup"),
    path("token/",ObtainAuthToken.as_view(),name="token"),
    # path("logout/",views.sign_out,name="logout"),

    
]+router.urls
