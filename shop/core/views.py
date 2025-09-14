from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db import connection
import logging

logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["GET"])
def health_check(request):
    """
    Health check endpoint that bypasses tenant middleware.
    This endpoint is used by Docker health checks and load balancers.
    """
    try:
        # Test database connectivity
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            cursor.fetchone()
        
        return JsonResponse({
            "status": "healthy",
            "service": "shop-backend",
            "database": "connected"
        }, status=200)
    
    except Exception as e:
        logger.error(f"Health check failed: {str(e)}")
        return JsonResponse({
            "status": "unhealthy",
            "service": "shop-backend",
            "error": str(e)
        }, status=503)
