from django.contrib import admin
from django.http import HttpResponse
from django.urls import re_path, path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions


def redirect_base_to_admin(request):
    return redirect("admin/")


schema_view = get_schema_view(
    openapi.Info(
        title="BRB Titans API",
        default_version="v1",
        description="brb-titans backend api",
        terms_of_service="https://www.google.com/policies/terms/",
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# External packages urls
urlpatterns = [path("rosetta/", include("rosetta.urls"))]

# Custom urls
urlpatterns += [
    path("api/users/", include("apps.users.urls")),
    path("api/events/", include("apps.events.urls")),
    path("api/anons/", include("apps.anons.urls")),
    path("api/approvals/", include("apps.approvals.urls")),
    path("api/chats/", include("apps.chats.urls")),
    path("api/tasks/", include("apps.planners.urls")),
]

# if not settings.DEBUG:
#     urlpatterns += [path("api/bot/", include("apps.bot.urls"))]

# Swagger urls
urlpatterns += [
    path(
        "swagger<format>/", schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

# Admin urls
urlpatterns += [
    path("", redirect_base_to_admin),
    path("admin/", admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
