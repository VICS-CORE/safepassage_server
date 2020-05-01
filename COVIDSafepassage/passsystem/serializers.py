from rest_framework import serializers
from .models import Pass, User, Organisation, Roles, Vehicle, Identity, Team


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class IdentitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Identity
        fields = '__all__'

    def create(self, validated_data):
        return Identity.objects.create(**validated_data)


class OrganisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = '__all__'

    def create(self, validated_data):
        return Organisation.objects.create(**validated_data)


class RolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = '__all__'

    def create(self, validated_data):
        return Roles.objects.create(**validated_data)


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def create(self, validated_data):
        return Vehicle.objects.create(**validated_data)


class PassSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pass
        fields = '__all__'

    def create(self, validated_data):
        return Pass.objects.create(**validated_data)


class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = '__all__'

    def create(self, validated_data):
        return Team.objects.create(**validated_data)












