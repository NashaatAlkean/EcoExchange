from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

from .models import User,Profile

#admin.site.register(User)
admin.site.unregister(Group)


class ProfileInline(admin.StackedInline):
    model=Profile


class UserAdmin(admin.ModelAdmin):
    model=User

    fields=["email","is_superuser","is_seeker","is_donor"]
    inlines=[ProfileInline]


admin.site.register(User,UserAdmin)