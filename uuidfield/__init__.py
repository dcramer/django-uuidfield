from __future__ import absolute_import
try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-uuidfield').version
except Exception as e:
    VERSION = 'unknown'
    
from .fields import UUIDField