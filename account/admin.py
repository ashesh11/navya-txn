from django.contrib import admin
from account.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'role']
    readonly_fields = ['email', 'name', 'created_at', 'updated_at']
    fields = ['email', 'name', 'created_at', 'updated_at', 'role']
    list_editable = ['role']
    list_filter = ['role']

    def has_add_permission(self, request):
        return False