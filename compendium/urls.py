from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='index'),

    url(r'^shop/(\d+)', views.shop, name='shop'),

    url(r'^shop/book/(\d+)', views.book_details, name='book_details'),
    url(r'^shop/misc/(\d+)', views.misc_details, name='misc_details'),
    url(r'^shop/apparel/(\d+)', views.apparel_details, name='apparel_details'),

    url(r'^trick_shop/(\d+)', views.trick_shop, name='trick_shop'),
    url(r'^trick_shop/trick/(\d+)', views.trick_details, name='trick_details'),

    url(r'^hire_us/(\d+)', views.hire_us, name='hire_us'),
    url(r'^hire_us/reviews(\d+)', views.reviews, name='reviews'),
    url(r'^hire_us/act(\d+)', views.act_details, name='act_details'),

    url(r'^add/(\d+)(\d+)', views.add_to_cart, name='add_to_cart'),
    url(r'^remove/(\d+)(\d+)', views.remove_from_cart, name='remove_from_cart'),
    url(r'^cart/', views.cart, name='cart'),

    url(r'^process/(\w+)', views.process_order, name='process_order'),
    url(r'^checkout/(\w+)', views.checkout, name='checkout'),
    url(r'^order_error/', views.order_error, name='order_error'),
    url(r'^complete_order/(\w+)', views.complete_order, name='complete_order'),

    url(r'^shipping_info/', views.shipping_info, name='shipping_info'),

    url(r'^contact_us/', views.contact_us, name='contact_us'),

]