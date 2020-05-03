from django.contrib import admin
from .models import Pass, User, Organisation, Roles, Vehicle, Identity, Team
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory


class AdminUserView(admin.ModelAdmin):

    model = User
    readonly_fields = ('user_id',)
    list_display = ['user_phonenumber', 'user_firstname', 'user_lastname', 'user_gender', 'user_teamid',
                    'user_createdon', 'user_image', 'user_address_zipcode']


class AdminIdentityView(admin.ModelAdmin):

    model = Identity
    readonly_fields = ('identity_id',)
    list_display = ['identity_id', 'identity_idtype', 'identity_idnumber', 'identity_createdon','identity_createdby']


class AdminOrganisationView(admin.ModelAdmin):

    model = Organisation
    readonly_fields = ('organisation_id',)
    list_display = ['organisation_phonenumber', 'organisation_primaryuser', 'organisation_name', 'organisation_address',
                    'organisation_createdon']


class AdminRolesView(admin.ModelAdmin):

    model = Roles
    # readonly_fields = ('roles_rolename',)
    list_display = ['roles_rolename', 'roles_roledescription', 'roles_passread', 'roles_passwrite', 'roles_teamread',
                    'roles_teamwrite', 'roles_createdon']


class AdminVehicleView(admin.ModelAdmin):

    model = Vehicle
    readonly_fields = ('vehicle_id',)
    list_display = ['vehicle_vehiclenumber', 'vehicle_id', 'vehicle_uid', 'vehicle_createdon','vehicle_createdby']


class AdminPassView(admin.ModelAdmin):

    model = Pass
    readonly_fields = ('pass_id',)
    list_display = ['pass_issuedto', 'pass_id', 'pass_issuedby', 'pass_passtype', 'pass_passreason', 'pass_radius',
                    'pass_createdon', 'pass_expirydate', 'pass_validitystate', 'pass_medicalverification']


class AdminTeamView(TreeAdmin, admin.ModelAdmin):
    readonly_fields = ('team_id',)
    fields = ['team_id', 'team_name', 'team_role', 'team_organisationid', 'team_createdon', '_position', '_ref_node_id']
    form = movenodeform_factory(Team)

    # def save_model(self, request, obj, form, change):
    #     obj.from_admin_site = True  # here we setting instance attribute which we check in `post_save`
    #     print("in admin")
    #     super().save_model(request, obj, form, change)


admin.site.register(Team, AdminTeamView)
admin.site.register(User, AdminUserView)
admin.site.register(Identity, AdminIdentityView)
admin.site.register(Organisation, AdminOrganisationView)
admin.site.register(Roles, AdminRolesView)
admin.site.register(Vehicle, AdminVehicleView)
admin.site.register(Pass, AdminPassView)
