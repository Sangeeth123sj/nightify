from django.urls import path, include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('home/', views.home, name='home'),
    path('converter/', views.converter, name='converter'),
    path('gallery/', views.gallery, name='gallery'),
    path('download/', views.download, name='download'),
    path('ajax/download/', views.download_ajax, name='download_ajax'),
    path('my_pictures/', views.my_pictures, name='my_pictures')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)