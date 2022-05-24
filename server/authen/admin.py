from django.contrib import admin
from .models import(roles )

@admin.register(roles)
class RolesAdmin(admin.ModelAdmin):
    '''
        Custom admin for roles model. 
        Admin will be able to view and edit the roles of users.
        id, username and role will be visible in admin.
    '''
    list_display = ['id', 'user', 'role']
# Register your models here.
