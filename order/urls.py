from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^payment/(?P<order_id>\d+)/(?P<pay_method>\w+)/$', views.pay_method, name='pay_method'),

]
