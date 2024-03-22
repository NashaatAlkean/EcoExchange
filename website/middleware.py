# middleware.py

from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect

class ImpersonateMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_id_to_impersonate = request.session.get('impersonate_id')
        if user_id_to_impersonate:
            try:
                user_to_impersonate = User.objects.get(pk=user_id_to_impersonate)
                if request.user.is_superuser:
                    # Save the current user in the session
                    request.session['real_user_id'] = request.user.id
                    # Log in as the user to impersonate
                    auth.login(request, user_to_impersonate)
            except User.DoesNotExist:
                pass

        response = self.get_response(request)

        return response
