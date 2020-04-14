from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user_id = models.AutoField(primary_key=True)
    user_createdon = models.DateTimeField(default=timezone.now)
    user_updatedon = models.DateTimeField(default=timezone.now)
    user_firstname = models.CharField(max_length=100)
    user_lastname = models.CharField(max_length=100, blank=True)
    user_middlename = models.CharField(max_length=100, blank=True)
    user_gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    user_image = models.ImageField(upload_to='', default='', blank=True)
    user_phonenumber = models.CharField(max_length=10, unique=True)
    user_altphonenumber = models.CharField(max_length=10, blank=True)
    user_addressid = models.IntegerField()
    user_identity = models.IntegerField()

    def __str__(self):
        return self.user_firstname


class Identity(models.Model):

    IDTYPE_CHOICES = [
        (0, 'AadharID'),
        (1, 'Driving License'),
        (2, 'PanCard Number'),
    ]

    identity_id = models.AutoField(primary_key=True)
    identity_idtype = models.IntegerField(choices=IDTYPE_CHOICES)
    identity_idnumber = models.CharField(max_length=100)
    identity_createdon = models.DateTimeField(default=timezone.now)
    identity_updateson = models.DateTimeField(default=timezone.now)
    identity_createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_identity_createdby')
    identity_updatedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_identity_updatedby')

    def __str__(self):
        return str(self.identity_id)


class Address(models.Model):

    address_id = models.AutoField(primary_key=True)
    address_name = models.CharField(max_length=1000)
    address_streetline1 = models.CharField(max_length = 1000)
    address_streetline2 = models.CharField(max_length=1000)
    address_streetline3 = models.CharField(max_length=1000)
    address_country = models.CharField(max_length=100)
    address_state = models.CharField(max_length=100)
    address_city = models.CharField(max_length=100)
    address_zipcode = models.CharField(max_length=10)
    address_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    address_longitude = models.DecimalField(max_digits=9, decimal_places=6)

    def __str__(self):
        return self.address_name


class Organisation(models.Model):

    organisation_id = models.AutoField(primary_key=True)
    organisation_primaryuser = models.CharField(max_length=500)
    organisation_name = models.CharField(max_length=1000)
    organisation_address = models.IntegerField()
    organisation_phonenumber = models.CharField(max_length=10, unique=True)
    organisation_altphonenumber = models.CharField(max_length=10, blank=True)
    organisation_updatedon = models.DateTimeField(default=timezone.now)
    organisation_createdon = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.organisation_name


class Roles(models.Model):

    ROLE_CHOICES = [
        (0, 'Citizen'),
        (1, 'Admin'),
        (2, 'Issuer'),
        (3, 'Scanner'),
    ]
    roles_orid = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='organisation_roles_ordid')
    roles_userid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles_userid')
    roles_rolename = models.IntegerField(choices=ROLE_CHOICES, primary_key=True)
    roles_roledescription = models.CharField(max_length=10000)
    roles_createdon = models.DateTimeField(default=timezone.now)
    roles_updatedon = models.DateTimeField(default=timezone.now)
    roles_isvalid = models.BooleanField(default=False)
    roles_createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles_createdby')
    roles_updatedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles_updatedby')

    def __str__(self):
        return str(self.roles_rolename)


class Vehicle(models.Model):

    vehicle_id = models.AutoField(primary_key=True)
    vehicle_uid = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_vehicle_uid')
    vehicle_vehiclenumber = models.CharField(max_length=50, unique=True)
    vehicle_vehicletype = models.CharField(max_length=100)
    vehicle_orgid = models.IntegerField(blank=True)
    vehicle_createdon = models.DateTimeField(default=timezone.now)
    vehicle_updatedon = models.DateTimeField(default=timezone.now)
    vehicle_createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_vehicle_createdby')

    def __str__(self):
        return self.vehicle_vehiclenumber


class Pass(models.Model):
    PASS_CHOICES = [
        (0, 'Pending'),
        (1, 'Approved'),
        (2, 'Expired'),
        (3, 'Revoked'),
    ]
    PASS_TYPE = [
        ('P', 'Permanent'),
        ('O', 'OneTime'),
        ('T', 'Temporary'),
    ]
    PASS_STATE_VALIDITY = [
        ('TN', 'Tamil Nadu'),
        ('KE', 'Kerala'),
        ('AP', 'Andhra Pradesh'),
        ('KA', 'Karnataka'),
        ('TE', 'Telangana'),
        ('NIL', 'Nil'),
    ]
    PASS_MEDICAL_VERIFICATION = [
        ('Y', 'required'),
        ('N', 'notrequired'),
    ]
    pass_id = models.AutoField(primary_key=True)
    pass_issuedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pass_issuedby')
    pass_issuedto = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pass_issuedto')
    pass_passtype = models.CharField(max_length=2, choices=PASS_TYPE, default='O')
    pass_passreason = models.CharField(max_length=20000)
    pass_createdon = models.DateTimeField(default=timezone.now)
    pass_expirydate = models.DateTimeField(default=timezone.now)
    pass_validitystate = models.IntegerField(choices=PASS_CHOICES, default=0)
    pass_updatedon = models.DateTimeField(default=timezone.now)
    pass_createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pass_createdby')
    pass_zipcode = models.CharField(max_length=10)
    pass_radius = models.CharField(max_length=1000)
    pass_updatedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pass_updaedby')
    pass_medicalverification = models.CharField(max_length=2, choices=PASS_MEDICAL_VERIFICATION, default='N')


    def __str__(self):
        return str(self.pass_issuedto)

