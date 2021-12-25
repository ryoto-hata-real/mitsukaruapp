from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from mainapp.models import User

class CustomUserAdmin(UserAdmin):
    add_fieldsets = (
        (None, {
            'fields': (
                'name',
                'email',
                'password',
            )
        }),
    )
    fieldsets = (
        (None, {
            'fields': (
                'name',
                'email',
                'password',
            )
        }),
        (None, {
            'fields':(
                'is_active',
                'is_admin',
            )
        })
    )

    list_display = ('email', 'is_active')
    list_filter = ()
    ordering = ()
    filter_horizontal = ()

admin.site.unregister(Group)
admin.site.register(User, CustomUserAdmin)
