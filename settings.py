
import os
TEMPLATE_DIRS += (os.path.join(  os.path.dirname(__file__), 'templates') ,)

STATICFILES_DIRS = (
os.path.dirname(__file__)+STATIC_URL,
)