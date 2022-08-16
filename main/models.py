from email.policy import default
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

class AutoTime(models.Model):
    name = models.CharField(max_length=l, verbose_name="Nomi")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

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
    status = models.CharField(max_length=l, default="maktab", null=True)

    def __str__(self):
        return f"{super().name}-{self.status}"


class Kollej(AutoTime):
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman")

    def __str__(self):
        return super().__str__()

class Universitet(AutoTime):
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Qaysi tuman")

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

class Bitiruvchi(models.Model):
    f_name = models.CharField(max_length=l, verbose_name="F.I.Sh")
    img = models.ImageField(default='default/default.png', upload_to='bitiruvchilar-foto/')
    t_sana = models.DateField(verbose_name="Tug'ulgan sana", null=True, blank=True)
    phone = models.CharField(max_length=9, verbose_name="(+998) ")
    email = models.EmailField(max_length=l, verbose_name="E-Pochta", null=True, blank=True)
    tuman = models.ForeignKey(TumanVaShahar, on_delete=models.CASCADE, verbose_name="Yashaydigan tuman(shahar)")
    mahalla = models.ForeignKey(Mahalla, on_delete=models.CASCADE, verbose_name="Mahalla Nomi")
    imkonyat = models.ManyToManyField(Imkonyat, related_name="abilty", verbose_name="Qoshimcha bilimi")
    qiziqish = models.ForeignKey(Qiziqish, related_name="interest", on_delete=models.CASCADE, verbose_name="Qiziqish")
    chettili = models.ManyToManyField(ChetTili, related_name="f_lang")
    guvohnoma = models.CharField(verbose_name="Haydovchilik Guvohnomasi", max_length=l, choices=yesNo, default="Yoq")
    idea = models.CharField(verbose_name="Biznes g'oya", max_length=l, choices=yesNo, default="Bor")
    short_f = models.CharField(max_length=10000, verbose_name="Bizness g'oya haqqida qisqacha (agar bor bo'lsa)", null=True, blank=True)
    jins = models.CharField(max_length=l, choices=jins, verbose_name="Jinsi", default="o'g'il bola")
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.f_name

    

class MaktabBitiruvchisi(Bitiruvchi):
    maktab = models.ForeignKey(Maktab, on_delete=models.CASCADE, verbose_name="Bitirayotgan maktab")
    sinf = models.CharField(max_length=l, choices=sinf, default='9-sinf', verbose_name="Sinf")
    univer_sity = models.CharField(max_length=l, verbose_name="Topshirmoqchi bo'lgan universitet", null=True, blank=True)

    def __str__(self):
        return super().__str__()

class KollejBitiruvchisi(Bitiruvchi):
    kollej = models.ForeignKey(Kollej, on_delete=models.CASCADE, verbose_name="Bitirayotgan Kollej")
    maqsad = models.CharField(max_length=l, choices=aim, default="Ishlamoqchi", verbose_name="Maqsadi")
    univer_sity = models.CharField(max_length=l, verbose_name="Topshirmoqchi bo'lgan universitet", null=True, blank=True)

    def __str__(self):
        return super().__str__()

class UniversitetBitiruvchisi(Bitiruvchi):
    maqsad = models.CharField(max_length=l, choices=aim, default="Ishlamoqchi", verbose_name="Maqsadi")
    universitet = models.ForeignKey(Universitet, on_delete=models.CASCADE, verbose_name="Bitirayotgan OTM", null=True, blank=True)

    def __str__(self):
        return super().__str__()


