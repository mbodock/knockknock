import base64

from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse


class BaseAuth(View):
    """Requires Base auth authentication"""

    def dispatch(self, request):
        if 'HTTP_AUTHORIZATION' not in request.META:
            return self.unauthorized()

        credentials = request.META['HTTP_AUTHORIZATION'].split(' ')
        if len(credentials) != 2 or credentials[0].lower() != "basic":
            return self.unauthorized()

        user, password = base64.b64decode(credentials[1]).decode('utf8').split(':', 1)
        if not user or not password:
            return self.unauthorized()

        return super().dispatch(request)

    def unauthorized(self):
        response = HttpResponse('', status=401)
        response['WWW-Authenticate'] = 'Basic Realm="restricted area"'
        return response


class UpdateHosts(BaseAuth):

    def post(self, request):
        pass
