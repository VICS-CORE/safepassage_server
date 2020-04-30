import datetime
import time

from django.shortcuts import render
from rest_framework import exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from COVIDSafepassage.auth_helpers import verify_id_token, create_session_cookie, create_token
from COVIDSafepassage.permission import IsAuthenticated
from .models import Pass, User, Organisation, Roles, Vehicle, Identity, Team
from .serializers import UserSerializer, IdentitySerializer, RolesSerializer, OrganisationSerializer,PassSerializer, \
    VehicleSerializer, TeamSerializer


def home(request):
    return render(request, 'passsystem/home.html')


class SessionLoginApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):

        idToken = request.data.get('idToken')
        if idToken is None:
            raise exceptions.AuthenticationFailed('Invalid Authentication Token')

        verified_claims = verify_id_token(idToken)
        # Only process if the user signed in within the last 5 minutes.
        if time.time() - verified_claims['auth_time'] < 5 * 60:
            expires_in = datetime.timedelta(days=5)
            expires = datetime.datetime.now() + expires_in
            session_cookie = create_session_cookie(idToken, expires_in)
            response = Response({'Login Success'}, status=status.HTTP_200_OK)
            response.set_cookie('SESSION',
                                session_cookie,
                                expires=expires,
                                httponly=True)
            return response

        raise exceptions.AuthenticationFailed('Recent sign in required')


class SessionLogoutApiView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response({'Logout Success'}, status=status.HTTP_200_OK)
        response.set_cookie('SESSION', expires=0)
        return response


class UserApiView(APIView):

#citizen-profile = 1
#issuer = 2
#scanner = 3
#citizen-passes = 4

    permission_classes = [IsAuthenticated]

    def get(self, request):
        phonenumber, usertype = request.GET['user_phonenumber'], request.GET['usertype']
        if phonenumber == '1111111111':
            if usertype == '2':
                    user1 = User.objects.all()
                    serializer = UserSerializer(user1, many=True)
                    return Response({"userpass": serializer.data})
            else:
                return Response({"access error"})
        else:
            if usertype == '3':
                tempuser = User.objects.get(user_phonenumber=phonenumber)
                user1 = tempuser.user_pass_issuedto.all()
                serializer1 = PassSerializer(user1, many=True)
                user2 = User.objects.filter(user_phonenumber=phonenumber)
                serializer2 = UserSerializer(user2, many=True)
                return Response({"user":serializer2.data , "userpass": serializer1.data})
            elif usertype == '4':
                tempuser = User.objects.get(user_phonenumber=phonenumber)
                user1 = tempuser.user_pass_issuedto.all()
                serializer = PassSerializer(user1, many=True)
                return Response({"userpass": serializer.data})
            elif usertype == '1':
                user1 = User.objects.filter(user_phonenumber=phonenumber)
                serializer = UserSerializer(user1, many=True)
                return Response({"user": serializer.data})
            else:
                return Response({"access error"})

    def post(self, request):
        user2 = request.data.get('user')
        serializer = UserSerializer(data=user2)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
            return Response({"success": "saved to user, user_phonenumber is '{}'".format(user_saved.user_phonenumber)})
        return Response({"ERROR": "unable to save user!"})


class IdentityApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        identityid = request.GET['identity_id']
        if identityid == '1':
            identity1 = Identity.objects.all()
        else:
            identity1 = Identity.objects.filter(identity_id=identityid)

        serializer = IdentitySerializer(identity1, many=True)
        return Response({"identity": serializer.data})

    def post(self, request):
        identity2 = request.data.get('identity')
        serializer = IdentitySerializer(data=identity2)
        if serializer.is_valid(raise_exception=True):
            identity_saved = serializer.save()
            return Response({"success": "saved to identity, identity_id is '{}'".format(identity_saved.identity_id)})
        return Response({"ERROR": "unable to save identity!"})


class OrganisationApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        phonenumber = request.GET['organisation_phonenumber']
        if phonenumber == '2222222222':
            organisation1 = Organisation.objects.all()
        else:
            organisation1 = Organisation.objects.filter(organisation_phonenumber=phonenumber)

        serializer = OrganisationSerializer(organisation1, many=True)
        return Response({"organisation": serializer.data})

    def post(self, request):
        organisation2 = request.data.get('organisation')
        serializer = OrganisationSerializer(data=organisation2)
        if serializer.is_valid(raise_exception=True):
            organisation_saved = serializer.save()
            return Response({"success": "saved to organisation, organisation_phonenumber is "
                                        "'{}'".format(organisation_saved.organisation_phonenumber)})
        return Response({"ERROR": "unable to save organisation!"})


class RolesApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        rolesrolename = request.GET['roles_rolename']
        if rolesrolename == '1':
            roles1 = Roles.objects.all()
        else:
            roles1 = Roles.objects.filter(roles_rolename=rolesrolename)

        serializer = RolesSerializer(roles1, many=True)
        return Response({"roles": serializer.data})

    def post(self, request):
        roles2 = request.data.get('roles')
        serializer = RolesSerializer(data=roles2)
        if serializer.is_valid(raise_exception=True):
            roles_saved = serializer.save()
            return Response({"success": "saved to roles, roles_rolename is '{}'".format(roles_saved.roles_rolename)})
        return Response({"ERROR": "unable to save roles!"})


class VehicleApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        vehiclenumber = request.GET['vehicle_vehiclenumber']
        if vehiclenumber == 'COVIDSP111':
            vehiclenumber1 = Vehicle.objects.all()
        else:
            vehiclenumber1 = Vehicle.objects.filter(vehicle_vehiclenumber=vehiclenumber)

        serializer = VehicleSerializer(vehiclenumber1, many=True)
        return Response({"vehicle": serializer.data})

    def post(self, request):
        vehicle2 = request.data.get('vehicle')
        serializer = VehicleSerializer(data=vehicle2)
        if serializer.is_valid(raise_exception=True):
            vehicle_saved = serializer.save()
            return Response({"success": "saved to vehicle, vehicle_id is '{}'".format(vehicle_saved.vehicle_id)})
        return Response({"ERROR": "unable to save vehicle!"})


class PassApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        passid = request.GET['pass_userphonenumber']
        if passid == '1111111111':
            pass1 = Pass.objects.all()
        else:
            pass1 = Pass.objects.filter(pass_issuedto__user_phonenumber=passid)

        serializer = PassSerializer(pass1, many=True)
        return Response({"pass": serializer.data})

    def post(self, request):
        pass2 = request.data.get('pass')
        serializer = PassSerializer(data=pass2)
        if serializer.is_valid(raise_exception=True):
            pass_saved = serializer.save()
            return Response({"success": "saved to pass, pass_user_id is '{}'".format(pass_saved.pass_id)})
        return Response({"ERROR": "unable to save pass!"})


class TeamApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        teamname = request.GET['team_name']
        if teamname == 'India-Admin':
            team1 = Team.objects.all()
            user1 = User.objects.all()
        else:
            team1 = Team.objects.filter(team_name=teamname)
            user1 = User.objects.filter(user_teamid__team_name=teamname)

        serializer1 = TeamSerializer(team1, many=True)
        serializer2 = UserSerializer(user1, many=True)
        return Response({"team": serializer1.data, "usersinteam": serializer2.data})

    def post(self, request):
        team1 = request.data.get('team')
        serializer = TeamSerializer(data=team1)
        if serializer.is_valid(raise_exception=True):
            team_saved = serializer.save()
            return Response({"success": "saved to team, team_id is '{}'".format(team_saved.team_id)})
        return Response({"ERROR": "unable to save team!"})


#======================================================================================================================#

# After Basic API for models


class IssuerIssuedPassApiView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        issuerid = request.GET['issuer_phone_number']
        if issuerid == '1111111111':
            pass1 = Pass.objects.all()
        else:
            pass1 = Pass.objects.filter(pass_issuedby__user_phonenumber=issuerid)

        serializer = PassSerializer(pass1, many=True)
        return Response({"pass": serializer.data})


