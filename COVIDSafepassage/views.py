from django.shortcuts import render



from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Issuer,Passes
from .serializers import issuerSerializer, passesSerializer

# Create your views here.

def home(request):
    return render(request, 'passsystem/home.html')


class issuerlist(APIView):

    def get(self, request):
        #issuer1 = Issuer.objects.all()
        issuer1 = Issuer.objects.filter(issuer_designation = 'M')

        serialzer = issuerSerializer(issuer1, many=True)
        return Response(serialzer.data)

    def post(self):
        pass


class passeslist(APIView):

    def get(self, request):
        phonenumber = request.GET['pass_phonenumber']
        if(phonenumber == '1111111111'):
            pass1 = Passes.objects.all()
        else:
            pass1 = Passes.objects.filter(pass_user_phonenumber=phonenumber)

        serialzer = passesSerializer(pass1, many=True)
        return Response(serialzer.data)

    def post(self):
        pass

# class passuserlist(APIView):
#
#     def get(self, request):
#         passuser1 = PassUser.objects.all()
#         serialzer = passuserSerializer(passuser1, many=True)
#         return Response(serialzer.data)
#
#     def post(self):
#         pass
#
