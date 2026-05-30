import time
import uuid
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.logger import logger

class LoggingAndTracingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Generate or capture unique correlation identifier
        request_id = request.headers.get("X-Request-ID", str(uuid.uuid4()))
        
        # Attach request_id to request state so controllers can access it
        request.state.request_id = request_id
        
        start_time = time.time()
        
        # Inject the identifier dynamically into the log records
        extra_tags = {"request_id": request_id}
        logger.info(f"Incoming: {request.method} {request.url.path}", extra=extra_tags)

        try:
            # Process request down the line to routes
            response = await call_next(request)
            
            process_time_ms = round((time.time() - start_time) * 1000, 2)
            
            # Record outcome metrics
            logger.info(
                f"Outgoing: {request.method} {request.url.path} | Status: {response.status_code} | Duration: {process_time_ms}ms", 
                extra=extra_tags
            )
            
            # Send correlation ID back to client in headers
            response.headers["X-Request-ID"] = request_id
            return response

        except Exception as exc:
            process_time_ms = round((time.time() - start_time) * 1000, 2)
            logger.error(
                f"Execution Fault: {request.method} {request.url.path} failed after {process_time_ms}ms. Detail: {str(exc)}", 
                extra=extra_tags, 
                exc_info=True
            )
            raise exc