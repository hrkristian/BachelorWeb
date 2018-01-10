from django.conf.urls import url

from .views import (Landing, Dagbok)
from organizer.views import Medlem

urlpatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
    url(r'^(?P<slug>[\w\-]+)/$', Dagbok.as_view(), name="dagbok")
]
