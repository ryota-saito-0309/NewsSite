"""
WSGI config for helloworld project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import sys  # 追加

from django.core.wsgi import get_wsgi_application

sys.path.append('E:/PUB_S/newssite')             # 追加
sys.path.append('E:/PUB_S/newssite/newssite')             # 追加

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "newssite.settings")

application = get_wsgi_application()