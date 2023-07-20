# Usersite/urls.py
from django.contrib.auth.views import LogoutView
from django.urls import path

from products.views import AddCategoryView, UpdateCategoryView, CategoriesList, CategoryDeleteView, AddProductView, \
    UpdateProductView, ProductDeleteView, ProductsList
from users.views import SignUpView, DashboardView

app_name = 'products'

urlpatterns = [
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    # update user url
    path('<int:pk>/update', UpdateCategoryView.as_view(), name='edit_category'),
    path('<int:pk>/delete', CategoryDeleteView.as_view(), name='delete_category'),

    path('categories_list/', CategoriesList.as_view(),
         name='categories_list'),  # user list url
    path('add_product/', AddProductView.as_view(), name="add_product"),
    # update user url
    path('<int:pk>/update_product', UpdateProductView.as_view(), name='edit_product'),
    path('<int:pk>/delete_product', ProductDeleteView.as_view(), name='delete_product'),

    path('products_list/', ProductsList.as_view(),
         name='products_list'),  # user list url
]