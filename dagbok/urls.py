from django.conf.urls import url

from .views import (Landing, Dagbok, PostCreate, PostEdit, PostDelete)
from organizer.views import Medlem

urlpatterns = [
    url(r'^$', Landing.as_view(), name='landing'),
    url(r'^(?P<slug>[\w\-]+)/$', Dagbok.as_view(), name="dagbok"),
    url(
        r'^(?P<slug>[\w\-]+)/new/$',
        PostCreate.as_view(),
        name="dagbok_post_create"
    ),
    url(
        r'^(?P<slug>[\w\-]+)/'
        r'(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<day>\d{1,2})/'
        r'edit/$',
        PostEdit.as_view(),
        name="dagbok_post_edit"
    ),
    url(

        r'^(?P<slug>[\w\-]+)/'
        r'(?P<year>\d{4})/'
        r'(?P<month>\d{1,2})/'
        r'(?P<day>\d{1,2})/'
        r'delete/$',
        PostDelete.as_view(),
        name="dagbok_post_delete"
    ),

]
