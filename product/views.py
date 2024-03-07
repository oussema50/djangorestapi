from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter
# Create your views here.
@api_view(['GET'])
def products(request):
    # allproducts = Product.objects.all()
    filterProducts = ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    # productSer = ProductSerializer(allproducts,many=True)
    productSer = ProductSerializer(filterProducts.qs,many=True)
    print(productSer)
    return Response({"products":productSer.data})

@api_view(['GET'])
def getProductById(request,id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    productSerialize = ProductSerializer(product,many=False)
    return Response({"product":productSerialize.data})
