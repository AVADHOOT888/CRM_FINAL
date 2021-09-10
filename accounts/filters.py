import django_filters
from django_filters.filters import DateFilter
from .models import *
from django_filters import DateFilter


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='date_created', lookup_expr='gte')
    exact_date = DateFilter(field_name='date_created', lookup_expr='iexact')
    end_date = DateFilter(field_name="date_created", lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['product', 'status']
