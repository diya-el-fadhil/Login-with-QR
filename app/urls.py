from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.user_login, name = 'user_login'),
    path('homepage',views.homepage, name = 'homepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)