from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import home, contacts

urlpatterns = [
                  path('', home),
                  path('contacts/', contacts)
              ] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
