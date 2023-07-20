"""filter for client"""
from datetime import datetime, timedelta

import django_filters
from django.db.models import Q, QuerySet, Value
from django.db.models.functions import Concat
from django_filters import FilterSet

from products.forms import CategoryFilterForm, ProductFilterForm


class CategoryFilter(FilterSet):
    search = django_filters.CharFilter(method='search_filter', label="Search")

    class Meta(CategoryFilterForm.Meta):
        pass

    def get_form_class(self):
        return CategoryFilterForm

    @staticmethod
    def search_filter(queryset: QuerySet, name: str, value: str) -> QuerySet:
        """
        method for search filter
        """
        return queryset.filter(
            Q(name__icontains=value)
        )


class ProductFilter(FilterSet):
    search = django_filters.CharFilter(method='search_filter', label="Search")

    class Meta(ProductFilterForm.Meta):
        pass

    def get_form_class(self):
        return ProductFilterForm

    @staticmethod
    def search_filter(queryset: QuerySet, name: str, value: str) -> QuerySet:
        """
        method for search filter
        """
        return queryset.filter(
            Q(name__icontains=value) |
            Q(product_code=value)
        )
