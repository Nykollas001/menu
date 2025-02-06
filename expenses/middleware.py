from .models import UserActivity

class UserActivityMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        
        if request.user.is_authenticated:
            # Get IP address
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            
            # Get or create activity record
            UserActivity.objects.update_or_create(
                user=request.user,
                ip_address=ip,
                defaults={
                    'user_agent': request.META.get('HTTP_USER_AGENT', ''),
                    'path': request.path
                }
            )
        
        return response
