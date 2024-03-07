import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    category = django_filters.CharFilter(field_name='category')
    price_gte = django_filters.filters.NumberFilter(field_name='price',lookup_expr='gte')
    price_lte = django_filters.NumberFilter(field_name='price',lookup_expr='lte')
    class Meta:
        model = Product
        fields = ['category','name','price_gte','price_lte']