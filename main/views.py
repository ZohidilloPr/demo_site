from django.shortcuts import redirect, render

from .models import (
    Mahalla, 
    TumanVaShahar, 
    MaktabBitiruvchisi, 
    KollejBitiruvchisi, 
    UniversitetBitiruvchisi,
    )

from .models import Maktab as MK
from .models import Kollej as KJ
from .forms import (
    MaktabForm,
    KollejForm,
    UniversitetForm,
)
# Create your views here.
list = [1, 2, 3, 4, 5]

# diagramm section

def Home(request):
    return render(request, 'base.html')

def Districts(request, pk):
    d = TumanVaShahar.objects.get(pk=pk)
    maktab = MK.objects.filter(tuman=pk).all()
    all_d = TumanVaShahar.objects.all().order_by('name')
    return render(request, "pages2/tumanlar.html", {
        'd':d,
        'pk':pk,
        'maktab':maktab,
        'all_d':all_d,
    })    

def Schools(request, pk):
    maktab = MK.objects.get(pk=pk)
    tuman_pk = MK.objects.get(pk=pk).tuman.pk
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    student = MaktabBitiruvchisi.objects.filter(maktab=maktab.pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    return render(request, "pages2/maktab/maktab.html",{
        'pk':pk,
        'all_d': all_d,
        'mk':maktab,
        'student':student,
        'all_mk':maktab_all,
        'all_kj': kollej_all,
    }) 

# tables section

def Table(request):
    mk = MaktabBitiruvchisi.objects.all()
    kj = KollejBitiruvchisi.objects.all()
    un = UniversitetBitiruvchisi.objects.all()
    return render(request, 'index.html', {
        "mk": mk,
        "kj": kj,
        "un": un,
    })

def Maktab(request):
    mk = MaktabBitiruvchisi.objects.all()
    return render(request, "pages/maktab.html", {
        'mk':mk,
    })

def Ish(request):
    return render(request, "pages/ish_.html")

def Kollej(request):
    kj = KollejBitiruvchisi.objects.all()
    return render(request, "pages/kollej.html", {
        'kj':kj,
    })

def OTM_Enter(request):
    return render(request, "pages/otm_topshirganlar.html")

def OTM_Finish(request):
    un = UniversitetBitiruvchisi.objects.all()
    return render(request, "pages/otm_bitiruvchilari.html", {
        'un':un,
    })

def Other(request):
    return render(request, "pages/boshqa.html")

# cv section

def Akmal(request):
    return render(request, 'cv/akmal.html')

def Bekmatov(request):
    return render(request, 'cv/bekmatov.html')

def Bekzod(request):
    return render(request, 'cv/bekzod.html')

def Dilshod(request):
    return render(request, 'cv/dilshod.html')

def Jasur(request):
    return render(request, 'cv/jasur.html')

def Akmal_(request):
    return render(request, 'pages2/cv/akmal.html')

def Bekmatov_(request):
    return render(request, 'pages2/cv/bekmatov.html')

def Bekzod_(request):
    return render(request, 'pages2/cv/bekzod.html')

def Dilshod_(request):
    return render(request, 'pages2/cv/dilshod.html')

def Jasur_(request):
    return render(request, 'pages2/cv/jasur.html')

def AllDistricts(request):
    all_d = TumanVaShahar.objects.all().order_by('name')
    return render(request, 'pages2/all_tumanlar.html', {"all_d": all_d })

# Add Sections

def DataAdd(request):
    return render(request, 'pages/data-add.html')

def MaktabAdd(request):
    if request.method == "POST":
        form = MaktabForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("MBA")
    form = MaktabForm
    return render(request, 'forms/add/maktabAdd.html', {"form":form})

def load_mahalla(request):
    tuman_id = request.GET.get('tuman_id')
    mahalla = Mahalla.objects.filter(tuman_id=tuman_id).order_by('name')
    return render(request, 'loads/load_mahalla_list.html', {"mahalla":mahalla})

def load_maktab(request):
    tuman_id = request.GET.get('tuman_id')
    maktab = MK.objects.filter(tuman_id=tuman_id).order_by("name")
    return render(request, 'loads/load_maktab_list.html', {"maktab" : maktab})

def KollejAdd(request):
    if request.method == "POST":
        form = KollejForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("KBA")
    form = KollejForm
    return render(request, 'forms/add/kollejAdd.html', {"form":form})

def load_kollej(request):
    tuman_id = request.GET.get("tuman_id")
    kollej = KJ.objects.filter(tuman_id=tuman_id).order_by('name')
    return render(request, 'loads/load_kollej_list.html', {"kollej":kollej})

def UniversitetAdd(request):
    if request.method == "POST":
        form = UniversitetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("UBA")
    form = UniversitetForm
    return render(request, 'forms/add/universitetAdd.html', {"form":form})