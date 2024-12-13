from django.urls import path
from .views import (
    ProductListView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView,
    api_product_list,
    api_product_detail,
)

urlpatterns = [
    path('', ProductListView.as_view(), name='products_list'),  # Displays all products
    path('create/', ProductCreateView.as_view(), name='product_create'),  # Create a new product
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),  # Update a product
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),  # Delete a product
    # API Endpoints
    path('api/products/', api_product_list, name='api_product_list'),
   
    path('api/products/<int:pk>/', api_product_detail, name='api_product_detail'),  # Correct pattern
]


