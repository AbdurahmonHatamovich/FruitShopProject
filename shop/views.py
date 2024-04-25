from django.views import View
from django.shortcuts import render, get_object_or_404
from shop.models import Fruit


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




