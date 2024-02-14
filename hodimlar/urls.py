from django.urls import path
from .views import hodimlar
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('hodimlar', hodimlar),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
