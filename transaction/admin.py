from django.contrib import admin
from transaction.models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['txn_id', 'name', 'transaction_date', 'approve_status']
    readonly_fields = ['txn_id', 'name', 'phone', 'email', 'amount', 'transaction_date']
    fields = ['txn_id', 'name', 'phone', 'email', 'amount', 'transaction_date', 'approve_status']
    list_editable = ['approve_status']
    list_filter = ['approve_status']

    def has_view_permission(self, request, obj=None):
        return request.user.is_staff or request.user.is_superuser
    
    def has_module_permission(self, request):
        return request.user.is_staff or request.user.is_superuser
    
    def has_change_permission(self, request, obj=None):
        return request.user.is_staff or request.user.is_superuser