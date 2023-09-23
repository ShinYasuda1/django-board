from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('bbs/', include('bbs.urls')),
    path('admin/', admin.site.urls),
]
