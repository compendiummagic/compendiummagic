from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^shop/(\d+)', views.shop, name='shop'),

    url(r'^shop/book/(\d+)', views.book_details, name='book_details'),
    url(r'^shop/misc/(\d+)', views.misc_details, name='misc_details'),
    url(r'^shop/apparel/(\d+)', views.apparel_details, name='apparel_details'),
]