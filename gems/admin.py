from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Contact)
admin.site.register(Review)


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'email', 'city']
