from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pass, User, Organisation, Roles, Address, Vehicle, Identity, Team
from .serializers import userSerializer, identitySerializer, rolesSerializer, organisationSerializer, addressSerializer,\
    passSerializer,vehicleSerializer, teamSerializer

from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType



from django.contrib.auth.models import Permission

# Create your views here.


def home(request):
    return render(request, 'passsystem/home.html')


class userapiview(APIView):
#citizen-profile = 1
#issuer = 2
#scanner = 3
#citizen-passes = 4
    def get(self, request):
        phonenumber, usertype = request.GET['user_phonenumber'], request.GET['usertype']
        if phonenumber == '1111111111':
            if usertype == '2':
                    user1 = User.objects.all()
                    serialzer = userSerializer(user1, many=True)
                    return Response({"userpass": serialzer.data})
            else:
                return Response({"access error"})
        else:
            if usertype == '3':
                tempuser = User.objects.get(user_phonenumber=phonenumber)
                user1 = tempuser.user_pass_issuedto.all()
                serialzer1 = passSerializer(user1, many=True)
                user2 = User.objects.filter(user_phonenumber=phonenumber)
                serialzer2 = userSerializer(user2, many=True)
                return Response({"user":serialzer2.data , "userpass": serialzer1.data})
            elif usertype == '4':
                tempuser = User.objects.get(user_phonenumber=phonenumber)
                user1 = tempuser.user_pass_issuedto.all()
                serialzer = passSerializer(user1, many=True)
                return Response({"userpass": serialzer.data})
            elif usertype == '1':
                user1 = User.objects.filter(user_phonenumber=phonenumber)
                serialzer = userSerializer(user1, many=True)
                return Response({"user": serialzer.data})
            else:
                return Response({"access error"})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):

        user2 = request.data.get('user')
        serializer = userSerializer(data=user2)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"success": "saved to user, user_phonenumber is '{}'".format(user_saved.user_phonenumber)})
        return Response({"ERROR": "unable to save user!"})


class identityapiview(APIView):

    def get(self, request):
        identityid = request.GET['identity_id']
        if identityid == '1':
            identity1 = Identity.objects.all()
        else:
            identity1 = Identity.objects.filter(identity_id=identityid)

        serialzer = identitySerializer(identity1, many=True)
        return Response({"identity": serialzer.data})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        identity2 = request.data.get('identity')
        serializer = identitySerializer(data=identity2)
        if serializer.is_valid(raise_exception=True):
            identity_saved = serializer.save()
            return Response({"success": "saved to identity, identity_id is '{}'".format(identity_saved.identity_id)})
        return Response({"ERROR": "unable to save identity!"})


class addressapiview(APIView):

    def get(self, request):
        addressid = request.GET['address_id']
        if addressid == '1':
            address1 = Address.objects.all()
        else:
            address1 = Address.objects.filter(address_id=addressid)

        serialzer = addressSerializer(address1, many=True)
        return Response({"address": serialzer.data})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        address2 = request.data.get('address')
        serializer = addressSerializer(data=address2)
        if serializer.is_valid(raise_exception=True):
            address_saved = serializer.save()
            return Response({"success": "saved to address, address_addressid is "
                                        "'{}'".format(address_saved.address_addressid)})
        return Response({"ERROR": "unable to save address!"})


class organisationapiview(APIView):

    def get(self, request):
        phonenumber = request.GET['organisation_phonenumber']
        if phonenumber == '2222222222':
            organisation1 = Organisation.objects.all()
        else:
            organisation1 = Organisation.objects.filter(organisation_phonenumber=phonenumber)

        serialzer = organisationSerializer(organisation1, many=True)
        return Response({"organisation": serialzer.data})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        organisation2 = request.data.get('organisation')
        serializer = organisationSerializer(data=organisation2)
        if serializer.is_valid(raise_exception=True):
            organisation_saved = serializer.save()
            return Response({"success": "saved to organisation, organisation_phonenumber is "
                                        "'{}'".format(organisation_saved.organisation_phonenumber)})
        return Response({"ERROR": "unable to save organisation!"})


class rolesapiview(APIView):

    def get(self, request):
        rolesrolename = request.GET['roles_rolename']
        if rolesrolename == '1':
            roles1 = Roles.objects.all()
        else:
            roles1 = Roles.objects.filter(roles_rolename=rolesrolename)

        serialzer = rolesSerializer(roles1, many=True)
        return Response({"roles": serialzer.data})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        roles2 = request.data.get('roles')
        serializer = rolesSerializer(data=roles2)
        if serializer.is_valid(raise_exception=True):
            roles_saved = serializer.save()
            return Response({"success": "saved to roles, roles_rolename is '{}'".format(roles_saved.roles_rolename)})
        return Response({"ERROR": "unable to save roles!"})


class vehicleapiview(APIView):

    def get(self, request):
        vehiclenumber = request.GET['vehicle_vehiclenumber']
        if vehiclenumber == 'COVIDSP111':
            vehiclenumber1 = Vehicle.objects.all()
        else:
            vehiclenumber1 = Vehicle.objects.filter(vehicle_vehiclenumber=vehiclenumber)

        serialzer = vehicleSerializer(vehiclenumber1, many=True)
        return Response({"vehicle": serialzer.data})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        vehicle2 = request.data.get('vehicle')
        serializer = vehicleSerializer(data=vehicle2)
        if serializer.is_valid(raise_exception=True):
            vehicle_saved = serializer.save()
            return Response({"success": "saved to vehicle, vehicle_id is '{}'".format(vehicle_saved.vehicle_id)})
        return Response({"ERROR": "unable to save vehicle!"})


class passapiview(APIView):

    def get(self, request):
        passid = request.GET['pass_id']
        if passid == '1':
            pass1 = Pass.objects.all()
        else:
            pass1 = Pass.objects.filter(pass_issuedto=passid)

        serialzer = passSerializer(pass1, many=True)
        return Response({"pass": serialzer.data})

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def post(self, request):
        pass2 = request.data.get('pass')
        serializer = passSerializer(data=pass2)
        if serializer.is_valid(raise_exception=True):
            pass_saved = serializer.save()
            return Response({"success": "saved to pass, pass_user_id is '{}'".format(pass_saved.pass_id)})
        return Response({"ERROR": "unable to save pass!"})


class teamapiview(APIView):

    def get(self, request):
        teamid = request.GET['team_id']
        if teamid == '1':
            team1 = Team.objects.all()
        else:
            team1 = Team.objects.filter(team_id=teamid)

        serialzer = teamSerializer(team1, many=True)
        return Response({"team": serialzer.data})

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        team2 = request.data.get('team')
        serializer = teamSerializer(data=team2)
        if serializer.is_valid(raise_exception=True):
            team_saved = serializer.save()

            return Response({"success": "saved to team, team_id is '{}'".format(team_saved.team_id)})
        return Response({"ERROR": "unable to save team!"})

#
# if team_saved.team_role.roles_rolename == 1:
#     teamname = team_saved.team_name
#     new_group, created = Team.objects.get_or_create(name=teamname)
#     ct = ContentType.objects.get_for_model(Team)
#     permission = Permission.objects.create(codename='can_add_team',
#                                            name='Can add team',
#                                            content_type=ct)
#     new_group.permissions.add(permission)
#     print("permission added 1")
# elif team_saved.team_role.roles_rolename == 2:
#     new_group, created = Team.objects.get_or_create(name=team_saved.team_name)
#     ct = ContentType.objects.get_for_model(Team)
#     permission = Permission.objects.create(codename='can_add_team',
#                                            name='Can add team',
#                                            content_type=ct)
#     new_group.permissions.add(permission)
#     print("permission added 2")