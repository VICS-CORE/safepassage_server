from django.db import models
from django.utils import timezone

from treebeard.al_tree import AL_Node


class Roles(models.Model):
    ROLE_CHOICES = [
        (0, 'Citizen'),
        (1, 'Admin'),
        (2, 'Issuer'),
        (3, 'Scanner'),
    ]

    roles_rolename = models.IntegerField(choices=ROLE_CHOICES, primary_key=True)
    roles_roledescription = models.CharField(max_length=10000)
    roles_passread = models.BooleanField(default=False)
    roles_passwrite = models.BooleanField(default=False)
    roles_teamread = models.BooleanField(default=False)
    roles_teamwrite = models.BooleanField(default=False)
    roles_createdon = models.DateTimeField(default=timezone.now)
    roles_updatedon = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.roles_rolename)


class Organisation(models.Model):

    organisation_id = models.AutoField(primary_key=True)
    organisation_primaryuser = models.CharField(max_length=500)
    organisation_name = models.CharField(max_length=1000)
    organisation_address = models.CharField(max_length=5000)
    organisation_phonenumber = models.CharField(max_length=10, unique=True)
    organisation_altphonenumber = models.CharField(max_length=10, blank=True)
    organisation_updatedon = models.DateTimeField(default=timezone.now)
    organisation_createdon = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.organisation_name


class Team(AL_Node):

    parent = models.ForeignKey('self',
                               related_name='children_set',
                               null=True,
                               db_index=True, on_delete=models.CASCADE, blank=True)
    team_id = models.AutoField(primary_key=True)
    node_order_by = ['team_id']
    team_organisationid = models.ForeignKey(Organisation, on_delete=models.CASCADE, related_name='team_organisationid')
    team_role = models.ForeignKey(Roles, on_delete=models.CASCADE, related_name='team_role')
    team_createdon = models.DateTimeField(default=timezone.now)
    team_updatedon = models.DateTimeField(default=timezone.now)

    # team_createdby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_vehicle_createdby')
    team_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.team_name


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
    user_address_name = models.CharField(max_length=1000, default="DoorOrHouseNumber")
    user_address_streetline1 = models.CharField(max_length=1000, default="Addressline1")
    user_address_streetline2 = models.CharField(max_length=1000, default="Addressline2")
    user_address_streetline3 = models.CharField(max_length=1000, blank=True)
    user_address_country = models.CharField(max_length=100, default="India")
    user_address_state = models.CharField(max_length=100, default="Tamil Nadu")
    user_address_city = models.CharField(max_length=100, default="Coimbatore")
    user_address_zipcode = models.CharField(max_length=10, default="641001")
    user_address_latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    user_address_longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    user_identity = models.IntegerField(blank=True)
    user_teamid = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='user_teamid', null=True, blank=True)

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
    pass_medicalverification = models.CharField(max_length=2, choices=PASS_MEDICAL_VERIFICATION, default='N')
    pass_updatedby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pass_updaedby')

    def __str__(self):
        return str(self.pass_issuedto)



















