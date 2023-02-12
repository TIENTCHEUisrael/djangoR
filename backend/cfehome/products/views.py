from django.shortcuts import render
from rest_framework import generics
from products.serializers import ProductSerializer

from products.models import Product

# Create your views here.


class ProductDetailApiView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
product_detail_view=ProductDetailApiView.as_view()