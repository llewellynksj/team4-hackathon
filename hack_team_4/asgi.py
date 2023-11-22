"""
ASGI config for hack_team_4 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hack_team_4.settings')

application = get_asgi_application()


application = ProtocolTypeRouter(
    {
        "http": application,
        # Just HTTP for now. (We can add other protocols later.)
    }
)
