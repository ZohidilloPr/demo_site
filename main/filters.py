import django_filters

from .models import (
    Bitiruvchi,
    MaktabBitiruvchisi,
    KollejBitiruvchisi,
    UniversitetBitiruvchisi,
)
from .forms import (
    KollejFilterForm,
    MaktabFilterForm,
    UniversiterFilterForm,
) 
class MaktabFilter(django_filters.FilterSet):
    class Meta:
        model = MaktabBitiruvchisi
        fields = ('tuman', 'mahalla', 'maktab', 'sinf')
        form = MaktabFilterForm

class KollejFilter(django_filters.FilterSet):
    class Meta:
        model = KollejBitiruvchisi
        fields = ('tuman', 'mahalla')
        form = KollejFilterForm

class UniversitetFilter(django_filters.FilterSet):
    class Meta:
        model = UniversitetBitiruvchisi
        fields = ('tuman', 'mahalla')
        form = UniversiterFilterForm

class BitiruvchiFilter(django_filters.FilterSet):
    class Meta:
        model = Bitiruvchi
        fields = ('tuman', 'mahalla', 'maktabbitiruvchisi__maktab','maktabbitiruvchisi__sinf', 'kollejbitiruvchisi__kollej', 'universitetbitiruvchisi__universitet')