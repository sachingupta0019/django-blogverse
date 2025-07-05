from django.contrib import admin
from .models import UserProfile
# Register your models here.

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user__username","user__email","get_password",         "user__first_name","user__last_name", "phone","gender","address","photo")

    def get_password(self, obj):
        return obj.user.password

