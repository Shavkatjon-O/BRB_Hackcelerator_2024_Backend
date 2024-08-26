from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.users.views import (
    SignUpView,
    UserProfileUpdateView,
    UserProfileView,
)

urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("profile/", UserProfileView.as_view(), name="user_profile"),
    path(
        "profile/update/", UserProfileUpdateView.as_view(), name="user_profile_update"
    ),
    path("sign-up/", SignUpView.as_view(), name="sign_up"),
]
