from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product
from .forms import ProductForm
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from django.http import JsonResponse

# Web Views
class ProductListView(ListView):
    model = Product
    template_name = 'products_list.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product_form.html'
    success_url = reverse_lazy('products_list')


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('products_list')


# API Views
@api_view(['GET', 'POST'])
def api_product_list(request):
    """
    API to list all products or create a new product.
    """
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def api_product_detail(request, pk):
    """
    API to retrieve, update, or delete a single product by ID.
    """
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    if request.method == 'GET':
        # Retrieve product
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update product
        serializer = ProductSerializer(product, data=request.data, partial=True)  # Allow partial updates
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        # Delete product
        product.delete()
        return JsonResponse({'message': 'Product deleted successfully'}, status=204)