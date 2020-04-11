from rest_framework import serializers
from .models import Issuer, Passes


class issuerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Issuer
        fields = ['issuer_name', 'issuer_designation']


class passesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Passes
        fields = '__all__'


# class passuserSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = PassUser
#         fields = ['pass_issuer_id', 'pass_issued_time', 'pass_status']
