import django_filters
from items.models import Items


class Itemfilter(django_filters.FilterSet):
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model=Items
        fields=['title','city','item_type','catagory']
