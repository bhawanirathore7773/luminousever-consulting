from django.core.cache import cache
from django.conf import settings
CACHE_VERSION=getattr(settings,"CACHE_VERSION","1")
def site_key(name,*parts): return ":".join(["site",CACHE_VERSION,name,*[str(p) for p in parts]])
def invalidate(*keys): cache.delete_many(keys)
