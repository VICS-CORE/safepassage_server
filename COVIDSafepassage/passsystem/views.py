import datetime
import time

from django.shortcuts import render
from rest_framework import exceptions
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from COVIDSafepassage.auth_helpers import verify_id_token, create_session_cookie, create_token
from COVIDSafepassage.permission import IsAuthenticated
from .models import Pass, User, Organisation, Roles, Address, Vehicle, Identity
from .serializers import userSerializer, identitySerializer, rolesSerializer, organisationSerializer, addressSerializer, \
    passSerializer, vehicleSerializer


# Create your views here.


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
        rolesuserid = request.GET['roles_userid']
        if rolesuserid == '1':
            roles1 = Roles.objects.all()
        else:
            roles1 = Roles.objects.filter(roles_userid=rolesuserid)

        serialzer = rolesSerializer(roles1, many=True)
        return Response({"roles": serialzer.data})

    def post(self, request):
        roles2 = request.data.get('roles')
        serializer = rolesSerializer(data=roles2)
        if serializer.is_valid(raise_exception=True):
            roles_saved = serializer.save()
            return Response({"success": "saved to roles, roles_userid is '{}'".format(roles_saved.roles_userid)})
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

    def post(self, request):
        pass2 = request.data.get('pass')
        serializer = passSerializer(data=pass2)
        if serializer.is_valid(raise_exception=True):
            pass_saved = serializer.save()
            return Response({"success": "saved to pass, pass_user_id is '{}'".format(pass_saved.pass_id)})
        return Response({"ERROR": "unable to save pass!"})






