from functools import wraps
from django.http import HttpResponseForbidden

def editor_or_manager_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if (
            request.user.is_superuser or
            request.user.groups.filter(
                name__in=['Editor', 'Manager']
            ).exists()
        ):
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden("Access Denied")

    return wrapper


def manager_required(view_func):

    @wraps(view_func)
    def wrapper(request, *args, **kwargs):

        if (
            request.user.is_superuser or
            request.user.groups.filter(
                name='Manager'
            ).exists()
        ):
            return view_func(request, *args, **kwargs)

        return HttpResponseForbidden(
            "Only managers can access this page."
        )

    return wrapper