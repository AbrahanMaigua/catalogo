from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    # ex: /polls/
    path("", views.catalogo, name="index"),
    path("c", views.catalogo_1, name="catalogo"),

  
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
