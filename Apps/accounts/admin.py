"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
     #Mostrar datos en Django
    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    #para que los campos sean clikeables y lleven al detalle
    list_display_links = ('pk', 'user',)
    #Los campos son editables
    list_editable = ('phone_number', 'website', 'picture')

    #Barra de busqueda
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    #Filtros por fecha dependiendo el orden es cxomo aparecen
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )

    #acomodar la informacion
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified',)

#Especificar campos que no se podran editar 
class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    """Muestra si esta activo"""
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )



admin.site.unregister(User)
admin.site.register(User, UserAdmin)