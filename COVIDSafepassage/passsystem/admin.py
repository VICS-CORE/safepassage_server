from django.contrib import admin
from .models import Pass, User, Organisation, Roles, Address, Vehicle, Identity, Team

from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
# Register your models here.

from django.contrib.auth.models import Group, Permission
from rest_framework import permissions
from django.contrib.contenttypes.models import ContentType


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
    readonly_fields = ('roles_rolename',)
    list_display = ['roles_rolename', 'roles_roledescription', 'roles_passread', 'roles_passwrite', 'roles_teamread',
                    'roles_teamwrite', 'roles_createdon']


class adminvehicleview(admin.ModelAdmin):

    model = Vehicle
    readonly_fields = ('vehicle_id',)
    list_display = ['vehicle_vehiclenumber', 'vehicle_id', 'vehicle_uid', 'vehicle_createdon','vehicle_createdby']


class adminpassview(admin.ModelAdmin):

    model = Pass
    readonly_fields = ('pass_id',)
    list_display = ['pass_issuedto', 'pass_id', 'pass_issuedby', 'pass_passtype', 'pass_passreason', 'pass_radius',
                    'pass_createdon', 'pass_expirydate', 'pass_validitystate', 'pass_medicalverification']


class adminteamview(TreeAdmin, admin.ModelAdmin):
    readonly_fields = ('team_id','group_ptr')
    fields = ['team_id', 'team_organisationid', 'team_name', 'team_role', 'team_createdon', '_position', '_ref_node_id', 'permissions', 'group_ptr', 'name' ]
    form = movenodeform_factory(Team)

    def save_model(self, request, obj, form, change):
        obj.from_admin_site = True  # here we setting instance attribute which we check in `post_save`
        print("in admin")

        print(request.POST)
        request1 = request.POST.copy()
        new_group, created = Team.objects.get_or_create(team_name=request.POST.get("team_name"))
        print(new_group.team_id)
        print(new_group.permissions.all())
        ct = ContentType.objects.get_for_model(Pass)

        # Now what - Say I want to add 'Can add project' permission to new_group?
        permission = Permission.objects.filter(content_type=ct)

        new_group.permissions.set(permission)
        print(new_group.permissions.all())
        request1['permissions']: new_group.permissions.all()
        super().save_model(request1, obj, form, change)
        # print("SUCCESS post_save")



admin.site.register(Team, adminteamview)

admin.site.register(User, adminuserview)
admin.site.register(Identity, adminidentityview)
admin.site.register(Address, adminaddressview)
admin.site.register(Organisation, adminorganisationview)
admin.site.register(Roles, adminrolesview)
admin.site.register(Vehicle, adminvehicleview)
admin.site.register(Pass, adminpassview)
