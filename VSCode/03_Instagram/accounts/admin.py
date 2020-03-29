from django.contrib import admin
from accounts.models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('is_superuser', 'username', 'first_name', 'email', 'is_staff', 'profile_msg')

admin.site.register(User, UserAdmin)