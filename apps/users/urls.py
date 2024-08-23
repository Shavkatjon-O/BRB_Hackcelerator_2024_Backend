from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.users.views import SignupView, UserDetailView, UserDetailUpdateView


urlpatterns = [
    path("sign-in/", TokenObtainPairView.as_view(), name="token-obtain-pair"),
    path("sign-in/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    path("sign-up/", SignupView.as_view(), name="sign-up"),
    path("profile/", UserDetailView.as_view(), name="profile"),
    path("profile/update/", UserDetailUpdateView.as_view(), name="profile-update"),
]
