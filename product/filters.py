import django_filters
from .models import Product
class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    category = django_filters.CharFilter(field_name='category')
    price = django_filters.CharFilter(field_name='price',lookup_expr='gte')
    class Meta:
        model = Product
        fields = ['price', 'category'] 