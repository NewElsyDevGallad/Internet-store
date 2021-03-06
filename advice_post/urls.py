from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})/(?P<post_slug>[-\w]+)/$',
        views.post_detail,
        name='post_detail'),
    url(r'^searched$', views.post_search, name='post_search'),
]
