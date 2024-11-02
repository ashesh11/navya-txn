from django.contrib import admin, messages
from account.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'role']
    readonly_fields = ['email', 'name', 'created_at', 'updated_at']
    fields = ['email', 'name', 'created_at', 'updated_at', 'role']
    list_editable = ['role']
    list_filter = ['role']

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return False
    
    def save_model(self, request, obj, form, change):
        # Check if the role is being set to 'admin'
        if form.cleaned_data.get('role') == 'admin':
            obj.is_staff = True
            obj.is_superuser = True
        elif form.cleaned_data.get('role') == 'manager':
            obj.is_staff = True
            obj.is_superuser = False
        else:
            admin_count = UserAccount.objects.filter(is_superuser=True).count()
            if obj.is_superuser and admin_count == 1: # At least one admin required
                messages.error(request, "At least one admin account is required.")
                return
            
            obj.is_staff = False
            obj.is_superuser = False
        
        # Call the original save_model method
        super().save_model(request, obj, form, change)