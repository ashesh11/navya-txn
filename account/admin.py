from django.contrib import admin
from account.models import UserAccount


@admin.register(UserAccount)
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'permission']
    readonly_fields = ['email', 'name', 'created_at', 'updated_at']
    fields = ['email', 'name', 'created_at', 'updated_at', 'permission']
    list_editable = ['permission']
    list_filter = ['permission']

    def has_add_permission(self, request):
        return False