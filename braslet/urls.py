from django.urls import path
from .views import braslet
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('braslet', braslet,name = 'braslet'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
