import time
import logging
logger=logging.getLogger("performance")
class RequestTimingMiddleware:
    def __init__(self,get_response): self.get_response=get_response
    def __call__(self,request):
        started=time.perf_counter()
        response=self.get_response(request)
        elapsed=(time.perf_counter()-started)*1000
        if elapsed>=500: logger.warning("slow_request",extra={"path":request.path,"method":request.method,"duration_ms":round(elapsed,1),"status":response.status_code})
        return response
