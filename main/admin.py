from django.contrib import admin
from .models import (
    Mahalla, 
    Maktab, 
    Kollej,
    Imkonyat,
    Qiziqish,
    ChetTili,
    Universitet,
    TumanVaShahar,
    MaktabBitiruvchisi,
    KollejBitiruvchisi,
    UniversitetBitiruvchisi,
)
# Register your models here.

admin.site.register(TumanVaShahar)
admin.site.register(Mahalla)
admin.site.register(Maktab)
admin.site.register(Kollej)
admin.site.register(Universitet)
admin.site.register(Qiziqish)
admin.site.register(Imkonyat)
admin.site.register(ChetTili)
admin.site.register(MaktabBitiruvchisi)
admin.site.register(KollejBitiruvchisi)
admin.site.register(UniversitetBitiruvchisi)
