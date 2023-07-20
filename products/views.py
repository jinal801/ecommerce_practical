from django.contrib import messages
from django.db.models.query import QuerySet
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DeleteView

from products.constants import CATEGORY_DELETE_MSG, PRODUCT_DELETE_MSG
from products.filters import CategoryFilter, ProductFilter
from products.forms import CategoryForm, UpdateCategoryForm, ProductForm, UpdateProductForm
from products.models import Category, Product


# Create your views here.
class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('products:categories_list')
    template_name = 'add_category.html'


class UpdateCategoryView(UpdateView):
    model = Category
    form_class = UpdateCategoryForm
    success_url = reverse_lazy('products:categories_list')
    template_name = 'categorydetail.html'


class CategoryDeleteView(DeleteView):
    # specify the model you want to use
    model = Category
    success_url = reverse_lazy('products:categories_list')
    template_name = 'categorieslist.html'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        category_obj = Category.objects.get(id=instance.id)
        category_obj.delete()
        messages.success(request, CATEGORY_DELETE_MSG)
        return HttpResponseRedirect(reverse_lazy('products:categories_list'))


class CategoriesList(ListView):
    model = Category
    template_name = 'categorieslist.html'
    paginate_by = 15
    ordering = ["-created"]

    def get_queryset(self, **kwargs) -> QuerySet:
        queryset_filter = CategoryFilter(data=self.request.GET,
                                     request=self.request)
        self.filter_form = queryset_filter.form
        order_by = self.request.GET.get("order_by", "-created")
        return queryset_filter.qs.order_by(order_by)

    def get_paginate_by(self, queryset):
        """
        Get the number of items to paginate by, or ``None`` for no pagination.
        """
        self.paginate_by = self.request.GET.get('paginate_by',
                                                self.paginate_by)
        return self.paginate_by

    # pass dictionary of form objects of all users into the template
    # with user.id as key and form object as its value
    def get_context_data(self, *args, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(*args, **kwargs)
        context["category_filter"] = self.filter_form
        return context


class AddProductView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:products_list')
    template_name = 'add_product.html'


class UpdateProductView(UpdateView):
    model = Product
    form_class = UpdateProductForm
    success_url = reverse_lazy('products:products_list')
    template_name = 'productdetail.html'


class ProductDeleteView(DeleteView):
    # specify the model you want to use
    model = Product
    success_url = reverse_lazy('products:products_list')
    template_name = 'productslist.html'

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        product_obj = Product.objects.get(id=instance.id)
        product_obj.delete()
        messages.success(request, PRODUCT_DELETE_MSG)
        return HttpResponseRedirect(reverse_lazy('products:products_list'))


class ProductsList(ListView):
    model = Product
    template_name = 'productlist.html'
    paginate_by = 15
    ordering = ["-created"]

    def get_queryset(self, **kwargs) -> QuerySet:
        queryset_filter = ProductFilter(data=self.request.GET,
                                     request=self.request)
        self.filter_form = queryset_filter.form
        order_by = self.request.GET.get("order_by", "-created")
        return queryset_filter.qs.order_by(order_by)

    def get_paginate_by(self, queryset):
        """
        Get the number of items to paginate by, or ``None`` for no pagination.
        """
        self.paginate_by = self.request.GET.get('paginate_by',
                                                self.paginate_by)
        return self.paginate_by

    # pass dictionary of form objects of all users into the template
    # with user.id as key and form object as its value
    def get_context_data(self, *args, object_list=None, **kwargs) -> dict:
        context = super().get_context_data(*args, **kwargs)
        context["product_filter"] = self.filter_form
        return context
