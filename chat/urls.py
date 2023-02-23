from django.urls import path
from . import views
from django.urls import include, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from ajax_select import urls as ajax_select_urls

admin.autodiscover()

urlpatterns = [
    path('', views.index, name='index'),
    path('chat/<str:room_name>/', views.room, name='room'),
    re_path(r'^ajax_select/', include(ajax_select_urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

