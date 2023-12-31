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
    path("events", views.events, name="events"),
    path("add_review", views.add_review, name="add_review"),
    
    
    
    path("blogs", views.blogs, name="blogs"),
    path("blog/<str:slug>", views.blog, name="blog"),

    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)