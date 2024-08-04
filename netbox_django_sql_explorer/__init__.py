import os

from django.conf import settings
from extras.plugins import PluginConfig

class NetBoxDjangoSQLExplorer(PluginConfig):
    name = 'netbox_django_sql_explorer'
    verbose_name = 'NetBox Django SQL Explorer'
    description = 'Explore the NetBox models via SQL'
    version = '0.1'
    base_url = 'explorer'
    django_apps = ['explorer']
    middleware = [
            "netbox_django_sql_explorer.middleware.RestrictSQLExplorerAccessMiddleware",
    ]
    default_settings = {
        "EXPLORER_GROUP_NAME": "explorer_users"
    }

    def ready(self):
        from . import custom

        custom.add_template_dir()
        custom.create_group(custom.get_group())
        super().ready()

config = NetBoxDjangoSQLExplorer
