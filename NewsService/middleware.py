from django.conf import settings
from django.shortcuts import redirect

from news.models import User


class CheckRoleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request, *args, **kwargs):
        response = self.get_response(request)
        return response
