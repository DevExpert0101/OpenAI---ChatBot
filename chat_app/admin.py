from django.contrib import admin
from .models import User, Chat

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id','email', 'username','is_superuser','mobile')
    search_fields = ('email','is_admin')
admin.site.register(User,CustomUserAdmin)

admin.site.register(Chat)