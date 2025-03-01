from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Meep, Profile

# Register your models here.
admin.site.unregister(Group)

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ["username"]
    inlines = [ProfileInline]


admin.site.unregister(User)

admin.site.register(User, UserAdmin)

admin.site.register(Meep)
#admin.site.register(Profile)


