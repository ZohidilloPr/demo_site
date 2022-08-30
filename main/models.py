
from django.db import models
# Create your models here.


l = 300

t_sh = (
    ("tuman", "tuman"),
    ("shahar", "shahar"),
)

yesNo = (
    ("Bor", "Bor"),
    ("Yoq", "Yoq"),
)

sinf = (
    ("9-sinf", "9-sinf"),
    ("11-sinf", "11-sinf"),
)

jins = (
    ("o'g'il bola", "o'g'il bola"),
    ("qiz bola", "qiz bola"),
)
aim = (
    ("O'qishni davom etirmoqchi", "O'qishni davom etirmoqchi"),
    ("Ishlamoqchi", "Ishlamoqchi"),
)

type_school = (
    ("O'rta ta'lim maktabi", "O'rta ta'lim maktabi"),
    ("Ixtisoslashgan maktablar", "Ixtisoslashgan maktablar"),
)

class AutoTime(models.Model):
    name = models.CharField(max_length=l, verbose_name="Nomi")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TypeKollej(AutoTime):
    def __str__(self):
        return super().__str__()

class TumanVaShahar(AutoTime):
    status = models.CharField(max_length=l, choices=t_sh, default="shaxar")

    def __str__(self):
        return f"{super().name} {self.status}"
    
    def all_maktab(self):
        return self.maktab_set.all()

class Mahalla(AutoTime):
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman")

    def __str__(self):
        return f"{super().__str__()} MFY"

class Maktab(AutoTime):
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman")
    status = models.CharField(max_length=l, default="O'rta ta'lim maktabi", choices=type_school, blank=True, null=True)

    def __str__(self):
        return f"{super().name}-{self.status}"

class Kollej(AutoTime):
    type = models.ForeignKey(TypeKollej, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ta'lim muassasasi turi")
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman")

    def __str__(self):
        return super().__str__()

class Vil(AutoTime):
    """ Viloyatlar nomi """
    def __str__(self):
        return super().__str__()

class Universitet(AutoTime):
    """ Yangi OTM nomi qo'shish """
    viloyat = models.ForeignKey(Vil, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="viloyat nomi")    
    def __str__(self):
        return super().__str__() 

class Qiziqish(AutoTime):

    def __str__(self):
        return super().__str__()

class Imkonyat(AutoTime):

    def __str__(self):
        return super().__str__()

class ChetTili(AutoTime):
    
    def __str__(self):
        return super().__str__()

class Sport(AutoTime):
    def __str__(self):
        return super().__str__()

class DriverLicense(AutoTime):
    def __str__(self):
        return super().__str__()

class Bitiruvchi(models.Model):
    f_name = models.CharField(max_length=l, verbose_name="F.I.Sh")
    img  = models.ImageField(default='default/default.png', upload_to='bitiruvchilar-foto/', verbose_name="Rasm")
    t_sana = models.DateField(verbose_name="Tug'ulgan sana", null=True, blank=True)
    jins = models.CharField(max_length=l, choices=jins, verbose_name="Jinsi", default="o'g'il bola")
    # millat = models.CharField(max_length=l, null=True, blank=True)
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Yashaydigan tuman(shahar)")
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, verbose_name="Mahalla Nomi")
    uy = models.CharField(max_length=l, null=True, blank=True, verbose_name="Ko'cha nomi 45uy")
    phone = models.CharField(max_length=9, verbose_name="Telefon raqam (+998) ", null=True, blank=True)
    email = models.EmailField(max_length=l, verbose_name="E-Pochta", null=True, blank=True)
    imkonyat = models.ManyToManyField(Imkonyat, related_name="abilty", verbose_name="Kompyuter bilimi")
    qiziqish = models.ForeignKey(Qiziqish, related_name="interest", on_delete=models.CASCADE, verbose_name="Qiziqish")
    sport = models.ManyToManyField(Sport, related_name="sport", verbose_name="Qiziqadigan sport turi")
    chettili = models.ManyToManyField(ChetTili, related_name="f_lang")
    idea = models.CharField(verbose_name="Biznes g'oya", max_length=l, choices=yesNo, default="Yoq")
    short_f = models.CharField(max_length=10000, verbose_name="Bizness g'oya haqqida qisqacha (agar bor bo'lsa)", null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)


    # guvohnoma = models.CharField(verbose_name="Haydovchilik Guvohnomasi", max_length=l, choices=yesNo, default="Yoq")
    # t_sana = models.CharField(max_length=l, verbose_name="Tug'ulgan sana", null=True, blank=True)

    def __str__(self):
        return self.f_name

    

class MaktabBitiruvchisi(Bitiruvchi):
    tuman_mk = models.ForeignKey(TumanVaShahar, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Maktab manzili")
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE, verbose_name="Bitirayotgan maktab")
    sinf = models.CharField(max_length=l, choices=sinf, default='9-sinf', verbose_name="Sinf")
    # maqsad = models.CharField(max_length=l, choices=aim, null=True, blank=True, default="Ishlamoqchi", verbose_name="Maqsadi")

    vil = models.ForeignKey(Vil, related_name="mk_vil", on_delete=models.SET_NULL, null=True, blank=True, verbose_name="OTM manzili")
    otm_name = models.ForeignKey(Universitet, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Topshirmoqchi bo'lgan OTM Nomi")
    stu_way_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    other_un = models.CharField(max_length=l, verbose_name="ChetEl OTM nomi", null=True, blank=True)
    stu_way_ch = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")

    # kerakmas
    univer_sity = models.CharField(max_length=l, verbose_name="Topshirmoqchi bo'lgan universitet", null=True, blank=True)
    
    def __str__(self):
        return super().__str__()


class KollejBitiruvchisi(Bitiruvchi):
    type = models.ForeignKey(TypeKollej, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Professional ta'lim")
    tuman_kj = models.ForeignKey(TumanVaShahar, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Kollej manzili")
    kollej = models.ForeignKey(Kollej, on_delete=models.SET_NULL, verbose_name="Bitirayotgan Kollej", null=True, blank=True)
    stu_way = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    maqsad = models.CharField(max_length=l, choices=aim, default="Ishlamoqchi", verbose_name="Maqsadi")
    guvohnoma = models.ManyToManyField(DriverLicense, related_name="guvohnomaK", verbose_name="Haydovchilik Guvohnomasi")
    
    vil = models.ForeignKey(Vil, on_delete=models.SET_NULL, null=True, blank=True, related_name="kj_vil",)
    otm_name = models.ForeignKey(Universitet, on_delete=models.SET_NULL, null=True, blank=True)
    stu_way_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    other_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="chetel otm")
    stu_way_ch = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    
    #kerakmas
    kolleJ = models.CharField(max_length=l, null=True, blank=True, verbose_name="Bitirayotgan kollej")
    univer_sity = models.CharField(max_length=l, verbose_name="Topshirmoqchi bo'lgan universitet", null=True, blank=True)
    
    def __str__(self):
        return super().__str__()

class UniversitetBitiruvchisi(Bitiruvchi):
    vil = models.ForeignKey(Vil, on_delete=models.SET_NULL, null=True, blank=True)
    universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE, verbose_name="Bitirayotgan OTM", null=True, blank=True)
    stu_way = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    other_un = models.CharField(max_length=l, null=True, blank=True, verbose_name="ChetEl OTM")
    stu_way_ch = models.CharField(max_length=l, null=True, blank=True, verbose_name="Mutaxasislik")
    maqsad = models.CharField(max_length=l, choices=aim, default="Ishlamoqchi", verbose_name="Maqsadi")
    guvohnoma = models.ManyToManyField(DriverLicense, related_name="guvohnomaU", verbose_name="Haydovchilik Guvohnomasi")
    
    #kerak emas
    universiteT = models.CharField(max_length=l, null=True, blank=True, verbose_name="Bitirayotgan OTM",)

    def __str__(self):
        return super().__str__()


