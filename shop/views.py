from django.views import View
from django.shortcuts import render
from shop.models import Fruit,BestSell,Vegetable
from .serializers import FruitSerializer,VegetableSerializer,BestSellSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters


class ShopPageView(View):
    def get(self, request):
        return render(request, 'main/shop.html')



class ShopDetaiLPageView(View):
    def get(self, request):
        return render(request, 'main/shop-detail.html')


class CartPageView(View):
    def get(self, request):
        return render(request, 'main/cart.html')

class ChackOutPageView(View):
    def get(self, request):
        return render(request, 'main/chackout.html')

class TestimonialPageView(View):
    def get(self, request):
        return render(request, 'main/testimonial.html')

class NotFoundPageView(View):
    def get(self, request):
        return render(request, 'main/404.html')


class ContactPageView(View):
    def get(self, request):
        return render(request, 'main/contact.html')



class SearchResulPageView(View):
    def get(self, request):
        search = request.GET.get('search')
        fruit = Fruit.objects.all()  # Default queryset

        if search:  # If search query exists
            fruit = Fruit.objects.filter(title__icontains=search)

        context = {'fruit': fruit, 'search': search}
        return render(request, 'main/search_result.html', context)

class FruitPageApiView(ModelViewSet):
    queryset = Fruit.objects.all()
    serializer_class = FruitSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)


class BestSellPageApiView(ModelViewSet):
    queryset = BestSell.objects.all()
    serializer_class = BestSellSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)

class VegetablePageApiView(ModelViewSet):
    queryset = Vegetable.objects.all()
    serializer_class = VegetableSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title',)




