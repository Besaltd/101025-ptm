import time

from django.http import HttpRequest, HttpResponse
from rest_framework_simplejwt.tokens import TokenError, AccessToken, RefreshToken
from rest_framework_simplejwt.settings import api_settings


class TestRequestNotificationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest, *args, **kwargs):
        # Работаем с самим request можно что-то сделать перед тем, как получим ответ

        print("=" * 100)
        print("[TestRequestNotificationMiddleware] INCOMING REQUEST!!!!!!!!")
        print(f"REQUEST METHOD: {request.method}")
        print(f"REQUEST PATH: {request.path}")
        print(f"REQUEST FULL PATH: {request.get_full_path()}")
        print(f"FROM ANONYMOUS: {request.user is not None}")
        print("=" * 100)

        response = self.get_response(request)

        # можно что-то сделать ПОСЛЕ того, как получим ответ
        print("=" * 100)
        print("[TestRequestNotificationMiddleware] OUTGOING RESPONSE!!!!!!!!")
        print(f"REQUEST FULL PATH: {response.status_code}")
        print(f"RESPONSE DATA: {response.data}")
        print("=" * 100)

        return response