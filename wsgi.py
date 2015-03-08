from __future__ import unicode_literals

import os
import sys
import site

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]

site.addsitedir('/home/tan/.virtualenvs/md/lib/python2.7/site-packages')

sys.path.append(os.path.join(PROJECT_ROOT, ".."))

settings_module = "%s.settings" % PROJECT_ROOT.split(os.sep)[-1]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
