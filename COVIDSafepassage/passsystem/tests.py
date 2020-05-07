from django.test import TestCase

import factory
import factory.django
from passsystem.models import Pass, User, Organisation, Roles, Vehicle, Identity


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    #user_id = models.AutoField(primary_key=True)
    user_createdon = factory.Faker('date_time')
    user_updatedon = factory.Faker('date_time')
    user_firstname = factory.Faker('name')
    user_lastname = factory.Faker('name')
    user_middlename = factory.Faker('name')
    user_gender = factory.Faker(
        'random_element', elements=[x[0] for x in User.GENDER_CHOICES]
    )
    #user_image = models.ImageField(upload_to='', default='', blank=True)
    user_phonenumber = factory.Faker('phone_number')
    user_altphonenumber = factory.Faker('phone_number')
    user_identity = factory.Faker('random_number')
    #user_teamid = factory.SubFactory(TeamFactory)

    user_address_name = factory.Faker('street_address')
    user_address_streetline1 = factory.Faker('street_address')
    user_address_streetline2 = factory.Faker('street_address')
    user_address_streetline3 = factory.Faker('street_address')
    user_address_country = factory.Faker('country')
    user_address_state = factory.Faker('city')
    user_address_city = factory.Faker('city')
    user_address_zipcode = factory.Faker('random_number')
    user_address_latitude = factory.Faker('latitude')
    user_address_longitude = factory.Faker('longitude')


class IdentityFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Identity

    #identity_id = models.AutoField(primary_key=True)
    identity_idtype = factory.Faker(
        'random_element', elements=[x[0] for x in Identity.IDTYPE_CHOICES]
    )
    identity_idnumber = factory.Faker('random_number')
    identity_createdon = factory.Faker('date_time')
    identity_updateson = factory.Faker('date_time')
    identity_updatedby = factory.SubFactory(UserFactory)
    identity_createdby = factory.SubFactory(UserFactory)


class OrganisationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Organisation

    #user_id = models.AutoField(primary_key=True)
    organisation_primaryuser = factory.Faker('name')
    organisation_name = factory.Faker('name')
    organisation_address = factory.Faker('street_address')
    organisation_phonenumber = factory.Faker('phone_number')
    organisation_altphonenumber = factory.Faker('phone_number')
    organisation_updatedon = factory.Faker('date_time')
    organisation_createdon = factory.Faker('date_time')


# class RolesFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = Roles
#
#     roles_rolename = factory.Faker(
#         'random_element', elements=[x[0] for x in Roles.ROLE_CHOICES]
#     )
#     roles_passread = factory.Faker('pybool')
#     roles_passwrite = factory.Faker('pybool')
#     roles_teamread = factory.Faker('pybool')
#     roles_teamwrite = factory.Faker('pybool')
#     roles_roledescription = factory.Faker('text')
#     roles_createdon = factory.Faker('date_time')
#     roles_updatedon = factory.Faker('date_time')


class PassFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Pass

    pass_issuedby = factory.SubFactory(UserFactory)
    pass_issuedto = factory.SubFactory(UserFactory)
    pass_passtype = factory.Faker(
        'random_element', elements=[x[0] for x in Pass.PASS_TYPE]
    )
    pass_passreason = factory.Faker('text')
    pass_createdon = factory.Faker('date_time')
    pass_expirydate = factory.Faker('date_time')
    pass_validitystate = factory.Faker(
        'random_element', elements=[x[0] for x in Pass.PASS_CHOICES]
    )
    pass_updatedon = factory.Faker('date_time')
    pass_createdby = factory.SubFactory(UserFactory)
    pass_zipcode = factory.Faker('random_number')
    pass_radius = factory.Faker('city')
    pass_updatedby = factory.SubFactory(UserFactory)
    pass_medicalverification = factory.Faker(
        'random_element', elements=[x[0] for x in Pass.PASS_MEDICAL_VERIFICATION]
    )


class VehicleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Vehicle

    vehicle_uid = factory.SubFactory(UserFactory)
    vehicle_vehiclenumber = factory.Faker('word')
    vehicle_vehicletype = factory.Faker('word')
    vehicle_orgid = factory.Faker('random_number')
    vehicle_createdon = factory.Faker('date_time')
    vehicle_updatedon = factory.Faker('date_time')
    vehicle_createdby = factory.SubFactory(UserFactory)


# class RolesTestCase(TestCase):
#     for _ in range(1):
#         RolesFactory.create()
#         print("Roles test success", _)


class OrganisationTestCase(TestCase):
    for _ in range(1):
        OrganisationFactory.create()
        print("Organisation test success", _)

# class TeamTestCase(TestCase):
#     for _ in range(1):
#         TeamFactory.create()
#         print("Team test success", _)


class UserTestCase(TestCase):
    for _ in range(50):
        UserFactory.create()
        print("user test success", _)


class PassTestCase(TestCase):
    for _ in range(50):
        PassFactory.create()
        print("Pass test success", _)


class VehicleTestCase(TestCase):
    for _ in range(1):
        VehicleFactory.create()
        print("Vehicles test success", _)


class IdentityTestCase(TestCase):
    for _ in range(10):
        IdentityFactory.create()
        print("identity test success", _)



