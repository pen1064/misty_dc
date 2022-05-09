"""
WSGI config for misty_dc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import inspect
from apps.ml.registry import MLRegistry
from apps.ml.classifier.xgb_model import XGBClassifier
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'misty_dc.settings')

application = get_wsgi_application()

try:
    registry = MLRegistry()
    xgb = XGBClassifier()
    registry.add_algorithm(endpoint_name = 'classifier', alg_obj = xgb, alg_name = 'xgboost',
            alg_status = 'production', alg_ver='0.0.1', alg_owner='pusheen',alg_description='xgb 1', 
            alg_code = inspect.getsource(XGBClassifier))

except Exception as e:
    print('Exception while loading to registry.', str(e))

