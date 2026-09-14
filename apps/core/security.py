from django.core.cache import cache
def rate_limit(request,prefix,limit=5,window=300):
    forwarded=request.META.get("HTTP_X_FORWARDED_FOR","")
    ip=(forwarded.split(",")[0].strip() if forwarded else request.META.get("REMOTE_ADDR","unknown"))
    key=f"rl:{prefix}:{ip}"
    try:
        added=cache.add(key,1,window)
        if added:return True
        value=cache.incr(key)
        return value<=limit
    except Exception:
        return True
