from django.urls import path
from .views import sipochka
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('sipochka', sipochka),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
