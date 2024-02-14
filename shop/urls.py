from django.urls import path
from .views import index
from django.conf.urls.static import static
from django.conf import settings
from hodimlar.views import hodimlar
from ziraklar.views import ziraklar
from braslet.views import braslet
from sipochka.views import sipochka

urlpatterns = [
                  path('', index, name='index'),
                  path('ziraklar', ziraklar, name='ziraklar'),
                  path('braslet', braslet, name='braslet'),
                  path('sipochka', sipochka, name='sipochka'),
                  path('hodimlar', hodimlar, name='hodimlar'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
