from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Django Rest Framework
    # auth/login and auth/logout
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('backend.cursos.urls')),  # <-
]
