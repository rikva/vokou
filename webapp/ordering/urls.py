from django.conf.urls import patterns, url
from .views import ProductsView, ProductDetail, OrderDisplay, FinishOrder, OrdersDisplay, PayOrder, OrderSummary

urlpatterns = patterns('',
    url(r'^products/$', ProductsView.as_view(), name="view_products"),
    url(r'^product/(?P<pk>[0-9]+)/$', ProductDetail.as_view(), name="view_product"),
    url(r'^order/(?P<pk>[0-9]+)/$', OrderDisplay.as_view(), name="view_order"),
    url(r'^order/(?P<pk>[0-9]+)/finish/$', FinishOrder.as_view(), name="finish_order"),
    url(r'^order/(?P<pk>[0-9]+)/pay/$', PayOrder.as_view(), name="pay_order"),
    url(r'^order/(?P<pk>[0-9]+)/summary/$', OrderSummary.as_view(), name="order_summary"),
    url(r'^orders/$', OrdersDisplay.as_view(), name="view_orders"),
)