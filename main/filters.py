import django_filters

from .models import (
    MaktabBitiruvchisi,
    KollejBitiruvchisi,
    UniversitetBitiruvchisi,
)
from .forms import (
    KollejFilterForm,
    MaktabFilterForm,
)
class MaktabFilter(django_filters.FilterSet):
    class Meta:
        model = MaktabBitiruvchisi
        fields = ('tuman', 'mahalla', 'maktab')
        form = MaktabFilterForm

class KollejFilter(django_filters.FilterSet):
    class Meta:
        model = KollejBitiruvchisi
        fields = ('tuman', 'mahalla', 'kollej')
        form = KollejFilterForm