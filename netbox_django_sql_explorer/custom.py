from django.contrib.auth.models import Group
from django.conf import settings
from netbox_django_sql_explorer import NetBoxDjangoSQLExplorer 
from pathlib import Path

def create_group(group: str) -> None:
    """ Create a NetBox group. """
    _, created = Group.objects.get_or_create(name=group)
    if created:
        print(f"{group} group created")
    else:
        print(f"{group} group already exists")

def get_group() -> str:
    """ Get a group name from settings. """
    config = NetBoxDjangoSQLExplorer
    if settings.__getattr__("EXPLORER_GROUP_NAME"):
        return settings.__getattr__("EXPLORER_GROUP_NAME")
    else:
        return config.default_settings["EXPLORER_GROUP_NAME"]

def add_template_dir() -> None:
    """ Add the custom templates directory to override base.html. """
    plugin_templates_dir = Path(__file__).resolve().parent / 'templates'
    if str(plugin_templates_dir) not in settings.TEMPLATES[0]['DIRS']:
        settings.TEMPLATES[0]['DIRS'].insert(0, str(plugin_templates_dir))
