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

# class SearchResulPageView(View):
#     def get(self, request):
#         search = request.GET.get('search')
#         if not search:
#             fruits = Fruit.objects.all()
#             context = {
#                 'fruits': fruits, 'search': search
#             }
#             return render(request, 'main/404.html', context)
#         else:
#             fruits = Fruit.objects.filter(title__icontains=search)
#             if fruits:
#                 context = {
#                     'fruits': fruits, 'search': search
#                 }
#                 return render(request, 'main/search_result.html', context)
#             else:
#                 return render(request, 'main/404.html')
#
#     def get_object(self, fruit_id):
#         return get_object_or_404(Fruit, id=fruit_id)


class SearchResulPageView(View):
    def get(self, request):
        search = request.GET.get('search')
        fruits = Fruit.objects.all()  # Default queryset

        if search:  # If search query exists
            fruits = Fruit.objects.filter(title__icontains=search)

        context = {'fruits': fruits, 'search': search}
        return render(request, 'main/search_result.html', context)




# class SearchResultsList(ListView):
#     model = Fruit
#     template_name = 'main/search_result.html'
#     context_object_name = 'all_fruit'
#
#     def get_queryset(self):
#         query = self.request.GET.get('s')
#         return Fruit.objects.filter(
#             Q(title__icontains=query) | Q(body__icontains=query)
#         )
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['categories'] = Fruit.objects.all()
#         return context


    # def get(self, request):
    #     search = request.GET.get('search')
    #     if not search:
    #         fruits = Fruit.objects.all()
    #         context = {'fruits': fruits}
    #         return render(request, 'main/search.html', context)
    #     else:
    #         fruits = Fruit.objects.all(title__icontains=search)
    #         if fruits:
    #             context = {'fruits': fruits}
    #             return render(request, 'main/search.html', context)
    #         else:
    #             context = {'fruits': fruits}
    #             return render(request, 'main/404.html')