from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home', views.home,name='home'),
    path('', views.index,name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)