import sys
import os

from django.conf import settings

BASE_DIR = os.path.dirname(__file__)


settings.configure(
    DEBUG=True,
    SECRET_KEY = 'vnb-!ljbvl2o)=k@f98-_px$9sdi#4gabf5=0j2g&$uknhpmp',
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    TEMPLATES=(
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [],
            'APP_DIRS': True,
        },
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIRECTORY=os.path.join(BASE_DIR, 'pages'),
)

if __name__ == "__main__":
    from django.core.management import execute_from_command_line

execute_from_command_line(sys.argv)
