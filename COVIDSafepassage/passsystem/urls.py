from django.urls import path
from . import views

app_name = "passsystem"


urlpatterns = [
    path('', views.home, name='home'),
    path('user/', views.UserApiView.as_view(), name='userapi'),
    path('identity/', views.IdentityApiView.as_view(), name='identityapi'),
    path('organisation/', views.OrganisationApiView.as_view(), name='organisationapi'),
    path('roles/', views.RolesApiView.as_view(), name='rolesapi'),
    path('vehicle/', views.VehicleApiView.as_view(), name='vehicleapi'),
    path('pass/', views.PassApiView.as_view(), name='passapi'),
    path('team/', views.TeamApiView.as_view(), name='teamapi'),
    path('sessionLogin/', views.SessionLoginApiView.as_view(), name='sessionLogin'),
    path('sessionLogout/', views.SessionLogoutApiView.as_view(), name='sessionLogout'),
    path('issuerissuedpass/', views.IssuerIssuedPassApiView.as_view(), name='issuerissuedpassapi'),
]

