from django.shortcuts import redirect


def authentication_auth(get_response):
    def middleware(request):
        if not request.user.is_authenticated and not request.path.startswith('/api/v1/inventory-auth/login/'):
            return redirect('/api/v1/inventory-auth/login/?next=/api/v1/auth/')
        return get_response(request)

    return middleware

