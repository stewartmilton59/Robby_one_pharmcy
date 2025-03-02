from django.urls import path
from .views import branch_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', branch_list, name='branch_list'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
