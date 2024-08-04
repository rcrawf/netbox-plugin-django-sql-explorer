from django.urls import path, include
from django.conf import settings

from .views import (
        explorer_redirect,
    )

urlpatterns = (
    path('explorer/', explorer_redirect, name='explorer_redirect'),
)
