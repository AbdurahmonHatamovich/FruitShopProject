from django.urls import path
from .views import ShopPageView,ShopDetaiLPageView,ContactPageView,ChackOutPageView,CartPageView,TestimonialPageView,NotFoundPageView,SearchResulPageView

urlpatterns = [
    path('shop/',ShopPageView.as_view(),name='shop'),
    path('shopdetail/',ShopDetaiLPageView.as_view(),name='shopdetail'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('cart/',CartPageView.as_view(),name='cart'),
    path('testimonial/',TestimonialPageView.as_view(),name='testimonial'),
    path('checkout/',ChackOutPageView.as_view(),name='checkout'),
    path('notfound/',NotFoundPageView.as_view(),name='notfound'),
    path('search/',SearchResulPageView.as_view(),name='search'),

    ]
