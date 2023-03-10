from django.shortcuts import render, get_object_or_404
from .models import Category, Product

from django.views.generic import ListView, DetailView



class ProductListView(ListView):
    template_name = 'shop/product/list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        category_slug = self.kwargs.get('category_slug')
        if category_slug:
            self.category = get_object_or_404(Category, slug=category_slug)
            queryset = queryset.filter(category=self.category)
        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['category'] = self.category if hasattr(self, 'category') else None
        context['categories'] = Category.objects.all()
        return context
    

class ProductDetailView(DetailView):
    template_name = 'shop/product/detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        queryset = Product.objects.filter(available=True)
        id = self.kwargs.get('id')
        slug = self.kwargs.get('slug')
        print(id)
        print(slug)
        queryset = queryset.filter(id=id).filter(slug=slug)
        return queryset
    




##### function based views below
# def product_list(request, category_slug=None):
#     category = None
#     categories = Category.objects.all()
#     products = Product.objects.filter(available=True)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)
#     return render(request,
#         'shop/product/list.html',
#         {
#         'category' : category,
#         'categories' : categories,
#         'products': products
#         })


# def product_detail(request, id, slug):
#     product = get_object_or_404(Product, id=id, slug=slug, available=True)
#     return render(request, 
#                   'shop/product/detail.html',
#                   {'product' : product})