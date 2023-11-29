from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('', views.main_view, name='main'),
    path('download', views.main_view, name = 'download')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)