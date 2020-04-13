from rest_framework import serializers
from .models import Pass, User, Organisation, Roles, Address, Vehicle, Identity


class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        return User.objects.create(**validated_data)


class identitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Identity
        fields = '__all__'

    def create(self, validated_data):
        return Identity.objects.create(**validated_data)

class addressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address
        fields = '__all__'

    def create(self, validated_data):
        return Address.objects.create(**validated_data)


class organisationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Organisation
        fields = '__all__'

    def create(self, validated_data):
        return Organisation.objects.create(**validated_data)


class rolesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Roles
        fields = '__all__'

    def create(self, validated_data):
        return Roles.objects.create(**validated_data)


class vehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

    def create(self, validated_data):
        return Vehicle.objects.create(**validated_data)


class passSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pass
        fields = '__all__'

    def create(self, validated_data):
        return Pass.objects.create(**validated_data)














