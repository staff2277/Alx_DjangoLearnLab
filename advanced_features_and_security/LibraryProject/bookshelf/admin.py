from django.contrib import admin
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.admin import UserAdmin
from .models import Book, CustomUser, Article

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  
    list_filter = ('publication_year', 'author') 
    search_fields = ('title', 'author')


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

def setup_groups():
    editors_group, created = Group.objects.get_or_create(name='Editors')
    viewers_group, created = Group.objects.get_or_create(name='Viewers')
    admins_group, created = Group.objects.get_or_create(name='Admins')

    permissions = {
        'Editors': ['can_create', 'can_edit'],
        'Viewers': ['can_view'],
        'Admins': ['can_create', 'can_edit', 'can_delete', 'can_view'],
    }

    for group_name, perms in permissions.items():
        group = Group.objects.get(name=group_name)
        for perm_codename in perms:
            permission = Permission.objects.get(codename=perm_codename)
            group.permissions.add(permission)

setup_groups()