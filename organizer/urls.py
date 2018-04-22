from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import (Home, ProsjektSkisse, ProsjektBeskrivelse, ProsjektDocs, ProsjektStatus)

urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
    url(r'^docs/$', ProsjektDocs.as_view(), name='docs'),
    url(r'^skisse/$', ProsjektSkisse.as_view(), name='skisse'),
    url(r'^status/$',ProsjektStatus.as_view(), name='status'),
    url(r'^beskrivelse/$', ProsjektBeskrivelse.as_view(), name='beskrivelse'),
]
