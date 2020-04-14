from django.contrib import admin
from .models import Pass, User, Organisation, Roles, Address, Vehicle, Identity

# Register your models here.


class adminuserview(admin.ModelAdmin):

    model = User
    readonly_fields = ('user_id',)
    list_display = ['user_phonenumber', 'user_firstname', 'user_lastname', 'user_gender', 'user_createdon',
                    'user_addressid', 'user_identity', 'user_image']


class adminidentityview(admin.ModelAdmin):

    model = Identity
    readonly_fields = ('identity_id',)
    list_display = ['identity_id', 'identity_idtype', 'identity_idnumber', 'identity_createdon','identity_createdby']


class adminaddressview(admin.ModelAdmin):

    model = Address
    readonly_fields = ('address_id',)
    list_display = ['address_id', 'address_latitude', 'address_longitude', 'address_zipcode',
                    'address_city', 'address_state']


class adminorganisationview(admin.ModelAdmin):

    model = Organisation
    readonly_fields = ('organisation_id',)
    list_display = ['organisation_phonenumber', 'organisation_primaryuser', 'organisation_name', 'organisation_address',
                    'organisation_createdon']


class adminrolesview(admin.ModelAdmin):

    model = Roles
    list_display = ['roles_userid', 'roles_rolename', 'roles_roledescription', 'roles_createdon','roles_createdby',
                    'roles_isvalid']


class adminvehicleview(admin.ModelAdmin):

    model = Vehicle
    readonly_fields = ('vehicle_id',)
    list_display = ['vehicle_vehiclenumber', 'vehicle_id', 'vehicle_uid', 'vehicle_createdon','vehicle_createdby']


class adminpassview(admin.ModelAdmin):

    model = Pass
    readonly_fields = ('pass_id',)
    list_display = ['pass_issuedto', 'pass_id', 'pass_issuedby', 'pass_passtype','pass_passreason', 'pass_radius',
                    'pass_createdon', 'pass_expirydate', 'pass_validitystate', 'pass_medicalverification']


admin.site.register(User, adminuserview)
admin.site.register(Identity, adminidentityview)
admin.site.register(Address, adminaddressview)
admin.site.register(Organisation, adminorganisationview)
admin.site.register(Roles, adminrolesview)
admin.site.register(Vehicle, adminvehicleview)
admin.site.register(Pass, adminpassview)
