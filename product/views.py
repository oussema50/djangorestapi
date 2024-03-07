from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ProductSerializer
from .models import Product
from .filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
# Create your views here.
@api_view(['GET'])
def products(request):
    # allproducts = Product.objects.all()
    # productSer = ProductSerializer(allproducts,many=True)
    filterProducts = ProductFilter(request.GET,queryset=Product.objects.all().order_by('id'))
    count = filterProducts.qs.count()
    resPage = 2
    paginater = PageNumberPagination()
    paginater.page_size = resPage
    quetyset = paginater.paginate_queryset(filterProducts.qs,request)
    productSer = ProductSerializer(quetyset,many=True)
    print("getrequest==>",request.GET)
    return Response({"products":productSer.data,"productCount":count})

@api_view(['GET'])
def getProductById(request,id):
    # product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)
    productSerialize = ProductSerializer(product,many=False)
    return Response({"product":productSerialize.data})
