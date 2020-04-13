from django.urls import path
from . import views

app_name = "passsystem"


urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.userapiview.as_view(), name='userapi'),
    path('identity/', views.identityapiview.as_view(), name='identityapi'),
    path('address/', views.addressapiview.as_view(), name='addressapi'),
    path('organisation/', views.organisationapiview.as_view(), name='organisationapi'),
    path('roles/', views.rolesapiview.as_view(), name='rolesapi'),
    path('vehicle/', views.vehicleapiview.as_view(), name='vehicleapi'),
    path('pass/', views.passapiview.as_view(), name='passapi'),
]

