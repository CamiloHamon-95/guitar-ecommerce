from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.contrib import admin
from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user','phone','picture')
    list_display_links = ['pk','user',]
    list_editable = ['phone','picture']
    list_filter = ['user__is_staff','user__is_active',]
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone'
    )
    fieldsets = [
        ('General information',{'fields':['user','phone','picture']}),
        ('Date information',{'fields':['created','modified'],'classes':['collapse',]}),
        ('Extra information',{'fields':['address','id_card','country','province','city','postal_code'],'classes':['collapse',]}),
    ]
    
    readonly_fields = ('created', 'modified',)
    
class ProfileInline(admin.TabularInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
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