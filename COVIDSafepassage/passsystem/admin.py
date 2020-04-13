from django.contrib import admin
from .models import Pass, User, Organisation, Roles, Address, Vehicle, Identity

# Register your models here.
admin.site.register(User)
admin.site.register(Pass)
admin.site.register(Organisation)
admin.site.register(Roles)
admin.site.register(Address)
admin.site.register(Vehicle)
admin.site.register(Identity)
