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

from .filters import (
    KollejFilter,
    MaktabFilter,
    UniversitetFilter,
)

# Create your views here.
list = [1, 2, 3, 4, 5]

# diagramm section

def Home(request):
    mkb = MaktabBitiruvchisi.objects.all().count()
    kjb = KollejBitiruvchisi.objects.all().count()
    unb = UniversitetBitiruvchisi.objects.all().count()
    return render(request, 'base.html', {
        'mkb':mkb,
        'kjb':kjb,
        'unb':unb,
    })

def Districts(request, pk):
    d = TumanVaShahar.objects.get(pk=pk)
    maktab = MK.objects.filter(tuman=pk).all()
    kollej_all = KJ.objects.filter(tuman_id=pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    mkb = MaktabBitiruvchisi.objects.filter(tuman_id=pk).count()
    kjb = KollejBitiruvchisi.objects.filter(tuman_id=pk).count()
    unb = UniversitetBitiruvchisi.objects.filter(tuman_id=pk).count()    
    return render(request, "pages2/tumanlar.html", {
        'd':d,
        'pk':pk,
        'maktab':maktab,
        'all_d':all_d,
        'mkb':mkb,
        'kjb':kjb,
        'unb':unb,
        'all_kj':kollej_all,
    })    

def Schools(request, pk):
    maktab = MK.objects.get(pk=pk)
    tuman_pk = MK.objects.get(pk=pk).tuman.pk
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = MaktabBitiruvchisi.objects.filter(maktab=maktab.pk)
    gra_9 = MaktabBitiruvchisi.objects.filter(maktab=pk, sinf="9-sinf").count()
    gra_11 = MaktabBitiruvchisi.objects.filter(maktab=pk, sinf="11-sinf").count()
    grils = MaktabBitiruvchisi.objects.filter(maktab=pk, jins="qiz bola").count()
    boys = MaktabBitiruvchisi.objects.filter(maktab=pk, jins="o'g'il bola").count()
    return render(request, "pages2/maktab/maktab.html",{
        'pk':pk,
        'mk':maktab,
        'boys': boys,
        'grils': grils,
        'all_d': all_d,
        'gra_9': gra_9,
        'gra_11': gra_11,
        'student':student,
        'all_mk':maktab_all,
        'all_kj': kollej_all,
    }) 

def KollejD(request, pk):
    kollej = KJ.objects.get(pk=pk)
    tuman_pk = kollej.tuman.pk
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = KollejBitiruvchisi.objects.filter(kollej=kollej.pk)
    grils = KollejBitiruvchisi.objects.filter(kollej=pk, jins="qiz bola").count()
    boys = KollejBitiruvchisi.objects.filter(kollej=pk, jins="o'g'il bola").count()
    return render(request, 'pages2/maktab/kollej.html', {
        'pk':pk,
        'kj':kollej,
        'boys':boys,
        'all_d':all_d,
        'grils': grils,
        'student':student,
        'all_mk':maktab_all,
        'all_kj':kollej_all,

    })

def ResumeMaktab(request, pk):
    maktab_b = MaktabBitiruvchisi.objects.get(pk=pk)
    return render(request, 'cv/resume_maktab.html', {
        'object': maktab_b,
    })

def ResumeMaktabTable(request, pk):
    maktab_b = MaktabBitiruvchisi.objects.get(pk=pk)
    return render(request, 'cv/resume_maktab_table.html', {
        'object': maktab_b,
    })

# tables section

def Table(request):
    mk = MaktabBitiruvchisi.objects.all()
    kj = KollejBitiruvchisi.objects.all()
    un = UniversitetBitiruvchisi.objects.all()
    all_object = {}
    all_object.update(mk.__dict__)
    all_object.update(kj.__dict__)
    all_object.update(un.__dict__)
     
    return render(request, 'index.html', {
        "mk": mk,
        "kj": kj,
        "un": un,
        "a_obj":all_object,
    })

def Maktab(request):
    mk = MaktabBitiruvchisi.objects.all()
    mkFilter = MaktabFilter(request.GET, queryset=mk)
    mk = mkFilter.qs
    return render(request, "pages/maktab.html", {
        'mk':mk,
        'mkFil':mkFilter,
    })

def Kollej(request):
    kj = KollejBitiruvchisi.objects.all()
    kjFilter = KollejFilter(request.GET, queryset=kj)
    kj=kjFilter.qs
    return render(request, "pages/kollej.html", {
        'kj':kj,
        'mkFil':kjFilter,
    })

def OTM_Finish(request):
    un = UniversitetBitiruvchisi.objects.all()
    unFilters = UniversitetFilter(request.GET, queryset=un)
    un = unFilters.qs
    return render(request, "pages/otm_bitiruvchilari.html", {
        'un':un,
        'mkFil':unFilters,
    })


def OTM_Enter(request):
    mk = MaktabBitiruvchisi.objects.all()
    kj = KollejBitiruvchisi.objects.all()
    all_list = []
    for i in mk:
        if not i.univer_sity:
            pass
        else:
            all_list.append(i)
    return render(request, "pages/otm_topshirganlar.html", context={
        'all_list':all_list,
    })
    

def Ish(request):
    return render(request, "pages/ish_.html")




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