import os
import django.core.asgi


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'guitar_max.settings')
application = django.core.asgi.get_asgi_application()
