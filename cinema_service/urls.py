from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

from cinema.urls import router

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/cinema/", include((router.urls, "cinema"))),
] + debug_toolbar_urls()
