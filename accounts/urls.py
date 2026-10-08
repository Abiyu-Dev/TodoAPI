from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from .views import *

app_name = "accounts"

urlpatterns = [
    # Registration
    path("register/", RegisterView.as_view(), name="register"),

    # Login: POST {username, password} -> {access, refresh}
    path("login/", CustomTokenObtainPairView.as_view(), name="login"),

    # Refresh: POST {refresh} -> new {access, refresh} (rotation enabled)
    path("refresh/", TokenRefreshView.as_view(), name="refresh"),

    # Verify: POST {token} -> 200 if valid, 401 if not. Useful for SPAs
    # that want to check "is my stored token still good?" on app boot.
    path("verify/", TokenVerifyView.as_view(), name="verify"),

    # Currently authenticated user
    path("me/", MeView.as_view(), name="me"),
]