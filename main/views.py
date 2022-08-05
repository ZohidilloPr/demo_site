from django.shortcuts import redirect, render

from .models import Mahalla
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

def Districts(request):
    return render(request, "pages2/tumanlar.html")    

def Schools(request):
    return render(request, "pages2/maktab/maktab.html", context={"list":list}) 

# tables section

def Table(request):
    return render(request, 'index.html', {"list": list})

def Maktab(request):
    return render(request, "pages/maktab.html")

def Ish(request):
    return render(request, "pages/ish_.html")

def Kollej(request):
    return render(request, "pages/kollej.html")

def OTM_Enter(request):
    return render(request, "pages/otm_topshirganlar.html")

def OTM_Finish(request):
    return render(request, "pages/otm_bitiruvchilari.html")

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