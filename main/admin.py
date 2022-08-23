from django.contrib import admin
from .models import (
    Vil,
    Sport,
    Maktab, 
    Kollej,
    Mahalla, 
    Qiziqish,
    ChetTili,
    Imkonyat,
    TypeKollej,
    Universitet,
    TumanVaShahar,
    DriverLicense,
    MaktabBitiruvchisi,
    KollejBitiruvchisi,
    UniversitetBitiruvchisi,

)
# Register your models here.

admin.site.register(Vil)
admin.site.register(Sport)
admin.site.register(Maktab)
admin.site.register(Kollej)
admin.site.register(Mahalla)
admin.site.register(Qiziqish)
admin.site.register(Imkonyat)
admin.site.register(ChetTili)
admin.site.register(TypeKollej)
admin.site.register(Universitet)
admin.site.register(DriverLicense)
admin.site.register(TumanVaShahar)
admin.site.register(MaktabBitiruvchisi)
admin.site.register(KollejBitiruvchisi)
admin.site.register(UniversitetBitiruvchisi)
