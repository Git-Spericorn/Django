"""
Permission decorator
"""
from functools import wraps
from django.core.exceptions import PermissionDenied
from django.utils.decorators import available_attrs
from accounts.templatetags.emp_extras import check_is_admin, check_is_employee


def admin_perm(fun_name, *args, **kwargs):
    """
    Admin permission decorator
    """
    @wraps(fun_name, assigned=available_attrs(fun_name))
    def decors(request):
        """
            Default Admin permission decorator
        """
        user = request.user
        if check_is_admin(user) is True:
            return fun_name(request, args, *kwargs)
        else:
            raise PermissionDenied
    return decors


def emp_perm(fun_name, *args, **kwargs):
    """
    Employee permission decorator
    """
    @wraps(fun_name, assigned=available_attrs(fun_name))
    def decors(request):
        """
          Default Employee permission decorator
          """
        user = request.user
        if check_is_employee(user) is True:
            return fun_name(request, args, *kwargs)
        else:
            raise PermissionDenied
    return decors
