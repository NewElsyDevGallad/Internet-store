from django.urls import path, include
from django.contrib import admin
from shop import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('cart/', include(('cart.urls', 'cart'), namespace='cart')),
    # path('order/', include(('order.urls', 'order'), namespace='order')),
    path('catalog/', include(('shop.urls', 'shop'), namespace='shop')),
    path('advices/', include(('advice_post.urls', 'advice_post'), namespace='advice_post')),
]
