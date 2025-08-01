from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# Swagger schema view setup
schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel App API",
        default_version='v1',
        description="API for managing travel destinations",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# Redirect root URL to Swagger UI
def home_redirect(request):
    return redirect('schema-swagger-ui')

urlpatterns = [
    path('', home_redirect, name='home'),
    path('admin/', admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include('listings.urls')),  # Make sure 'listings' is your app
]
