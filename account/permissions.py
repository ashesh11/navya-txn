from rest_framework.permissions import BasePermission
from account.models import UserAccount


# Helper functions to check specific roles
def is_manager(user_id):
    return UserAccount.objects.filter(id=user_id, role='manager').exists()

def is_staff(user_id):
    return UserAccount.objects.filter(id=user_id, role='staff').exists()

def is_manager_or_staff(user_id):
    return UserAccount.objects.filter(id=user_id, role__in=['staff', 'manager']).exists()


class BasePermissionHandler(BasePermission):
    def check_permission(self, request, method_permissions):
        user_id = request.user.id
        check = method_permissions.get(request.method) #Retrieve function based on request method
        return check(user_id)


class TransactionListViewPermissionHandler(BasePermissionHandler):
    def has_permission(self, request, view):
        method_permissions = {
            'GET': is_manager_or_staff,
            'POST': is_manager_or_staff
        }

        return self.check_permission(request, method_permissions)
    

class TransactionDetailViewPermissionHandler(BasePermissionHandler):
    def has_permission(self, request, view):
        method_permissions = {
            'GET': is_manager_or_staff,
            'PUT': is_manager_or_staff,
            'PATCH': is_manager_or_staff,
            'DELETE': is_manager
        }

        return self.check_permission(request, method_permissions)