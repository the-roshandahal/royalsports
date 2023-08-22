from django.urls import path
from . import views
from django.urls import re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static  


urlpatterns = [
    path("", views.home, name="home"),
    path("contact", views.contact, name="contact"),
    path("join_rsc", views.join_rsc, name="join_rsc"),
    path("gallery", views.gallery, name="gallery"),
    path("gallery_details/<int:id>", views.gallery_details, name="gallery_details"),
    path("participation", views.participation, name="participation"),

]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)