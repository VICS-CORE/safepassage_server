from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pass, User, Organisation, Roles, Address, Vehicle, Identity
from .serializers import userSerializer, identitySerializer, rolesSerializer, organisationSerializer, addressSerializer, passSerializer,vehicleSerializer

# Create your views here.


def home(request):
    return render(request, 'passsystem/home.html')


class userapiview(APIView):

    def get(self, request):
        #user1 = User.objects.all()
        phonenumber = request.GET['user_phonenumber']
        if phonenumber == '1111111111':
            user1 = User.objects.all()
        else:
            user1 = User.objects.filter(user_phonenumber=phonenumber)

        serialzer = userSerializer(user1, many=True)
        return Response({"user": serialzer.data})

    def post(self, request):
        user2 = request.data.get('user')
        serializer = userSerializer(data=user2)
        if serializer.is_valid(raise_exception=True):
            user_saved = serializer.save()
        return Response({"success": "saved to user"})


class identityapiview(APIView):

    def get(self, request):
        #issuer1 = Issuer.objects.all()
        identityid = request.GET['identity_id ']
        identity1 = Identity.objects.filter(identity_id =identityid)

        serialzer = identitySerializer(identity1, many=True)
        return Response({"identity": serialzer.data})

    def post(self, request):
        identity2 = request.data.get('identity')
        serializer = identitySerializer(data=identity2)
        if serializer.is_valid(raise_exception=True):
            identity_saved = serializer.save()
        return Response({"success": "saved to identity"})


class addressapiview(APIView):

    def get(self, request):
        #issuer1 = Issuer.objects.all()
        addressid = request.GET['address_addressid']
        address1 = Address.objects.filter(address_id=addressid)

        serialzer = addressSerializer(address1, many=True)
        return Response({"address": serialzer.data})

    def post(self, request):
        address2 = request.data.get('address')
        serializer = addressSerializer(data=address2)
        if serializer.is_valid(raise_exception=True):
            address_saved = serializer.save()
        return Response({"success": "saved to address"})


class organisationapiview(APIView):

    def get(self, request):
        #issuer1 = Issuer.objects.all()
        phonenumber = request.GET['organisation_phonenumber']
        organisation1 = Organisation.objects.filter(organisation_phonenumber=phonenumber)

        serialzer = organisationSerializer(organisation1, many=True)
        return Response({"organisation": serialzer.data})

    def post(self, request):
        organisation2 = request.data.get('organisation')
        serializer = organisationSerializer(data=organisation2)
        if serializer.is_valid(raise_exception=True):
            organisation_saved = serializer.save()
        return Response({"success": "saved to organisation"})


class rolesapiview(APIView):

    def get(self, request):
        #issuer1 = Issuer.objects.all()
        rolesuserid = request.GET['roles_userid']
        roles1 = Roles.objects.filter(roles_userid=rolesuserid)

        serialzer = rolesSerializer(roles1, many=True)
        return Response({"roles": serialzer.data})

    def post(self, request):
        roles2 = request.data.get('roles')
        serializer = rolesSerializer(data=roles2)
        if serializer.is_valid(raise_exception=True):
            roles_saved = serializer.save()
        return Response({"success": "saved to roles"})


class vehicleapiview(APIView):

    def get(self, request):
        #issuer1 = Issuer.objects.all()
        vehiclenumber = request.GET['vehicle_vehiclenumber']
        vehiclenumber1 = Vehicle.objects.filter(vehicle_vehiclenumber=vehiclenumber)

        serialzer = vehicleSerializer(vehiclenumber1, many=True)
        return Response({"vehicle": serialzer.data})

    def post(self, request):
        vehicle2 = request.data.get('vehicle')
        serializer = vehicleSerializer(data=vehicle2)
        if serializer.is_valid(raise_exception=True):
            vehicle_saved = serializer.save()
        return Response({"success": "saved to vehicle"})


class passapiview(APIView):

    def get(self, request):
        passid = request.GET['pass_id']
        pass1 = Pass.objects.filter(pass_id=passid)

        serialzer = passSerializer(pass1, many=True)
        return Response({"pass": serialzer.data})

    def post(self, request):
        pass2 = request.data.get('pass')
        serializer = passSerializer(data=pass2)
        if serializer.is_valid(raise_exception=True):
            pass_saved = serializer.save()
        return Response({"success": "saved to pass"})

