from django.forms import ModelForm
from .models import Category, Product
from django import forms


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class CategoryFilterForm(forms.ModelForm):
    search = forms.CharField(required=False)

    class Meta:
        model = Category
        fields = [
            "name",
        ]


class UpdateCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'parent')


class ProductFilterForm(forms.ModelForm):
    search = forms.CharField(required=False)

    class Meta:
        model = Product
        fields = [
            "name",
        ]


class UpdateProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'owner', 'product_code', 'price', 'category', 'expiry_date')