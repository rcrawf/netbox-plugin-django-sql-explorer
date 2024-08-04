from django.contrib.auth.models import Group
from django.shortcuts import redirect

from netbox_django_sql_explorer import custom

GROUP_NAME = custom.get_group()
EXPLORER_PATHS = (
    "/explorer/",
    "/plugins/explorer/",
)

class UnauthorizedExplorerException(Exception):
    pass

class RestrictSQLExplorerAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(EXPLORER_PATHS) and not request.user.is_superuser:
            if not request.user.is_authenticated:
                return redirect('login')
            if not Group.objects.get(name=GROUP_NAME) in request.user.groups.all():
                raise UnauthorizedExplorerException(
                        f"{request.user} is not a member of the group: {GROUP_NAME}"
                )

        response = self.get_response(request)
        return response
