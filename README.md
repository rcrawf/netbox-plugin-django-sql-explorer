## NetBox Django SQL Explorer

NetBox plugin to install and configure [https://pypi.org/project/django-sql-explorer/](django-sql-explorer).

### Installation

Install from <TBC>

`settings.py`

```
EXPLORER_CONNECTIONS = {
    'Default': 'default'
}
EXPLORER_DEFAULT_CONNECTION = 'default'
EXPLORER_TASKS_ENABLED = False
EXPLORER_GROUP_NAME = "explorer_users"  #  optional

```

```
manage.py migrate
manage.py collectstatic
```

