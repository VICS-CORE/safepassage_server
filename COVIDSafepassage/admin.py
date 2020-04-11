from django.contrib import admin
from .models import Passes, Issuer

# Register your models here.
admin.site.register(Issuer)
admin.site.register(Passes)