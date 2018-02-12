from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import (Home, ProsjektSkisse, ProsjektBeskrivelse)

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^skisse/$', ProsjektSkisse.as_view(), name='skisse'),
    url(r'^beskrivelse/$', ProsjektBeskrivelse.as_view(), name='beskrivelse'),
]
