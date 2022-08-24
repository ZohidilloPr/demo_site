from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin

from .models import (
    Bitiruvchi,
    ChetTili,
    Imkonyat,
    Mahalla,
    Qiziqish,
    TypeKollej, 
    Universitet,
    TumanVaShahar, 
    MaktabBitiruvchisi, 
    KollejBitiruvchisi, 
    UniversitetBitiruvchisi,
    )

from .models import Maktab as MK
from .models import Kollej as KJ
from .forms import (
    KollejNameForm,
    MaktabForm,
    KollejForm,
    MaktabNameForm,
    UniversitetForm,
    UniversitetNameForm,
)

from .filters import (
    BitiruvchiFilter,
    KollejFilter,
    MaktabFilter,
    UniversitetFilter,
)

from django.views.generic.edit import (
    CreateView
)

from django.db.models import Q

# Create your views here.

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
def SearchAllStudents(request):
    mkb = MaktabBitiruvchisi.objects.all().count()
    kjb = KollejBitiruvchisi.objects.all().count()
    unb = UniversitetBitiruvchisi.objects.all().count()
    query = request.GET.get('searchHome')
    if query:
        queryset = Bitiruvchi.objects.filter(
            Q(f_name__icontains=query) |
            Q(tuman__name__icontains=query) |
            Q(mahalla__name__icontains=query) |
            Q(phone__icontains=query) |
            Q(jins__icontains=query) |
            Q(maktabbitiruvchisi__sinf__icontains=query) |
            Q(maktabbitiruvchisi__maktab__name__icontains=query) |
            Q(kollejbitiruvchisi__stu_way__icontains=query) |
            Q(universitetbitiruvchisi__stu_way__icontains=query) 
        ).order_by("f_name")
    else:
        queryset = Bitiruvchi.objects.all().order_by('f_name')        
    return render(request, 'pages/search.html', {
        'mkb':mkb,
        'kjb':kjb,
        'unb':unb,
        'queryset':queryset,
    })

def Districts(request, pk):
    d = TumanVaShahar.objects.get(pk=pk)
    maktab = MK.objects.filter(tuman=pk).all()
    kollej_all = KJ.objects.filter(tuman_id=pk)
    # uni_all = Universitet.objects.filter(tuman_id=pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    typeKol = TypeKollej.objects.all()
    mkb = MaktabBitiruvchisi.objects.filter(tuman_id=pk).count()
    kjb = KollejBitiruvchisi.objects.filter(tuman_id=pk).count()
    unb = UniversitetBitiruvchisi.objects.filter(tuman_id=pk).count()
    btr = Bitiruvchi.objects.filter(tuman_id=pk) 
    return render(request, "pages2/tumanlar.html", {
        'd':d,
        'pk':pk,
        'mkb':mkb,
        'unb':unb,
        'kjb':kjb,
        'all_btr':btr,
        'all_d':all_d,
        'maktab':maktab,
        # 'all_un':uni_all,
        'typeK': typeKol,
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

def AllKollejBit(request, pk):
    all_types = TypeKollej.objects.all()
    kollej_all_stu = KollejBitiruvchisi.objects.filter(tuman=pk)
    tuman_id = kollej_all_stu[0].tuman.pk
    kj = KJ.objects.filter(tuman_id=tuman_id)
    maktab_all = MK.objects.filter(tuman_id=tuman_id)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = KollejBitiruvchisi.objects.filter(tuman=pk)
    grils = KollejBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="qiz bola").count()
    boys = KollejBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="o'g'il bola").count()
    list_p_t = []
    for i in all_types:
        list_p_t.append(kollej_all_stu.filter(type=i.pk).count())
        print(kollej_all_stu.filter(type=i.pk).count())
    return render(request, "pages2/maktab/all_kollej_stu.html",{
        'pk':pk,
        'kjt': kj,
        'boys': boys,
        'grils': grils,
        'all_d': all_d,
        'student':student,
        'tuman_id':tuman_id,
        'all_mk':maktab_all,
        'kas':kollej_all_stu,
        'all_type':all_types,
        'count_0': list_p_t[0],
        'count_1': list_p_t[1],
        'count_2': list_p_t[2],
        #'all_kj': kollej_all,
    }) 

def OTM_all_stu(request, pk):
    otm_all_stu = UniversitetBitiruvchisi.objects.filter(tuman=pk)
    tuman_id = otm_all_stu[0].tuman.pk
    maktab_all = MK.objects.filter(tuman_id=tuman_id)
    all_d = TumanVaShahar.objects.all().order_by('name')
    student = UniversitetBitiruvchisi.objects.filter(tuman=pk)
    grils = UniversitetBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="qiz bola").count()
    boys = UniversitetBitiruvchisi.objects.filter(tuman_id=tuman_id, jins="o'g'il bola").count()
    return render(request, "pages2/maktab/all_otm_stu.html",{
        'pk':pk,
        'boys': boys,
        'grils': grils,
        'all_d': all_d,
        'kas':otm_all_stu,
        'student':student,
        'all_mk':maktab_all,
        'tuman_id':tuman_id,
        # 'all_kj': kollej_all,
    }) 

def KollejD(request, pk):
    all_types = TypeKollej.objects.all()
    kollej = KJ.objects.get(pk=pk)
    tuman_pk = kollej.tuman.pk
    kj = KJ.objects.filter(tuman_id=tuman_pk)
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    all_d = TumanVaShahar.objects.all().order_by('name')
    # univer_all = Universitet.objects.filter(tuman_id=tuman_pk)
    student = KollejBitiruvchisi.objects.filter(kollej=kollej.pk)
    grils = KollejBitiruvchisi.objects.filter(kollej=pk, jins="qiz bola").count()
    boys = KollejBitiruvchisi.objects.filter(kollej=pk, jins="o'g'il bola").count()
    return render(request, 'pages2/maktab/kollej.html', {
        'pk':pk,
        'kjt':kj,
        'kj':kollej,
        'boys':boys,
        'all_d':all_d,
        'grils': grils,
        'student':student,
        'all_mk':maktab_all,
        'all_kj':kollej_all,
        # 'all_un':univer_all,
        'all_type':all_types,

    })

def UniversitetB(request, pk):
    un = Universitet.objects.get(pk=pk)
    tuman_pk = un.tuman.pk
    all_d = TumanVaShahar.objects.all().order_by('name')
    students = UniversitetBitiruvchisi.objects.filter(universitet=un.pk)
    maktab_all = MK.objects.filter(tuman_id=tuman_pk)
    kollej_all = KJ.objects.filter(tuman_id=tuman_pk)
    # univer_all = Universitet.objects.filter(tuman_id=tuman_pk)
    grils = UniversitetBitiruvchisi.objects.filter(universitet=pk, jins="qiz bola").count()
    boys = UniversitetBitiruvchisi.objects.filter(universitet=pk, jins="o'g'il bola").count()
    return render(request, 'pages2/universitet.html', {
        'pk':pk,
        'un':un,
        'all_d':all_d,
        'student':students,
        'all_mk':maktab_all,
        'all_kj':kollej_all,
        # 'all_un':univer_all,
        'boys':boys,
        'grils':grils,

    })

# RESUME SECTIONS

def Resume(request, pk):
    object = Bitiruvchi.objects.get(pk=pk)
    return render(request, 'cv/resume.html', context={
        'pk' : pk,
        'object' : object,
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

def ResumeKollej(request, pk):
    kollej_b = KollejBitiruvchisi.objects.get(pk=pk)
    return render(request, 'cv/resume_kollej.html', {
        'object': kollej_b,
    })

def ResumeKollejTable(request, pk):
    kollej_b = KollejBitiruvchisi.objects.get(pk=pk)
    return render(request, 'cv/resume_kollej_table.html', {
        'object': kollej_b,
    })

def ResumeUniversitet(request, pk):
    univer_b = UniversitetBitiruvchisi.objects.get(pk=pk)
    return render(request, 'cv/resume_univer.html', {
        'object': univer_b,
    })

def ResumeUniversitetTable(request, pk):
    univer_b = UniversitetBitiruvchisi.objects.get(pk=pk)
    return render(request, 'cv/resume_univer_table.html', {
        'object': univer_b,
    })

# tables section

def Table(request):
    all_students = Bitiruvchi.objects.all()
    all_student_filter = BitiruvchiFilter(request.GET, queryset=all_students)
    all_students = all_student_filter.qs 
    return render(request, 'index.html', {
        'all_students':all_students,
        'mkFil':all_student_filter,
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
    for i in kj:
        if not i.univer_sity:
            pass
        else:
            all_list.append(i)
    return render(request, "pages/otm_topshirganlar.html", context={
        'all_list':all_list,
    })
    
def AllDistricts(request):
    all_d = TumanVaShahar.objects.all().order_by('name')
    return render(request, 'pages2/all_tumanlar.html', {"all_d": all_d })


def Ish(request):
    return render(request, "pages/ish_.html")

def Other(request):
    return render(request, "pages/boshqa.html")


# Add Sections

def DataAdd(request):
    return render(request, 'pages/data-add.html')

def MaktabAdd(request):
    if request.method == "POST":
        form = MaktabForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Maktab Muafaqiyatli qo'shildi")
            return redirect("MBA")
        messages.error(request, "Malumot kiritishda xatolik")
        
    form = MaktabForm
    imk = Imkonyat.objects.all()
    return render(request, 'forms/add/maktabAdd.html', {
        "form":form,
        'imk':imk,
    })

class KollejAdd(SuccessMessageMixin, CreateView):
    model = KollejBitiruvchisi
    form_class = KollejForm
    template_name = 'forms/add/kollejAdd.html'
    success_url = reverse_lazy("KBA")
    success_message = 'Kollej muaffaqiyatli qo\'shildi!'

# def KollejAdd(request):
#     if request.method == "POST":
#         form = KollejForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("KBA")
#     form = KollejForm
#     return render(request, 'forms/add/kollejAdd.html', {"form":form})

def UniversitetAdd(request):
    if request.method == "POST":
        form = UniversitetForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Universitet Muafaqiyatli qo'shildi")
            return redirect("UBA")
        messages.error(request, "Malumot kiritishda xatolik")
        
        
    form = UniversitetForm
    return render(request, 'forms/add/universitetAdd.html', {"form":form})

class MaktabNameAddView(SuccessMessageMixin, CreateView):
    model = MK
    template_name = 'forms/sections/add/maktabnameadd.html'
    form_class = MaktabNameForm
    success_message = 'Yangi maktab muaffaqiyatli qo\'shildi!'
    success_url = reverse_lazy("MaNAV")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Maktab'
        return context
        
class KollejNameAddView(SuccessMessageMixin, CreateView):
    model = KJ
    template_name = 'forms/sections/add/kollejnameadd.html'
    form_class = KollejNameForm
    success_url = reverse_lazy("KNAV")
    success_message = 'Yangi kollej muaffaqiyatli qo\'shildi!'


class UniversitetNameAddView(SuccessMessageMixin, CreateView):
    model = Universitet
    template_name = 'forms/sections/add/universitetnameadd.html'
    form_class = UniversitetNameForm
    success_url = reverse_lazy("UNAV")
    success_message = 'Yangi universitet muaffaqiyatli qo\'shildi!'


class QiziqishNameAddView(SuccessMessageMixin, CreateView):
    model = Qiziqish
    fields = '__all__'
    success_url = reverse_lazy("QNAV")
    template_name = 'forms/sections/add/qiziqishnameadd.html'
    success_message = 'Yangi qiziqish muaffaqiyatli qo\'shildi!'


class ImkonyatNameAddView(SuccessMessageMixin, CreateView):
    model = Imkonyat
    fields = '__all__'
    success_url = reverse_lazy("INAV")
    template_name = 'forms/sections/add/imkonyatnameadd.html'
    success_message = 'Yangi imkonyat muaffaqiyatli qo\'shildi!'


class ChetTiliNameAddView(SuccessMessageMixin, CreateView):
    model = ChetTili
    fields = '__all__'
    success_url = reverse_lazy("FNAV")
    template_name = 'forms/sections/add/f_langnameadd.html'
    success_message = 'Yangi chet tili muaffaqiyatli qo\'shildi!'
    

class MahallaNameAddView(SuccessMessageMixin, CreateView):
    model = Mahalla
    fields = '__all__'
    success_url = reverse_lazy("MNAV")
    template_name = 'forms/sections/add/mahallanameadd.html'
    success_message = 'Yangi mahalla muaffaqiyatli qo\'shildi!'

class TumanVaShaharNameAddView(SuccessMessageMixin, CreateView):
    model = TumanVaShahar
    fields = '__all__'
    success_url = reverse_lazy("TvSNAV")
    template_name = 'forms/sections/add/tumannameadd.html'
    success_message = 'Yangi Malumot muaffaqiyatli qo\'shildi!'


# AJAX SECTION

def load_kollej(request):
    tuman_id = request.GET.get("tuman_kj")
    kollej = KJ.objects.filter(tuman_id=tuman_id).order_by('name')
    return render(request, 'loads/load_kollej_list.html', {"kollej" : kollej})

def load_type_kollej(request):
    tuman_id = request.GET.get("tuman_kj")
    type = request.GET.get("type")
    kollej = KJ.objects.filter(tuman=tuman_id, type=type).order_by("name")
    return render(request, 'loads/load_type_kollej_list.html', {"kollej" : kollej})

def load_mahalla(request):
    tuman_id = request.GET.get('tuman_id')
    mahalla = Mahalla.objects.filter(tuman_id=tuman_id).order_by('name')
    return render(request, 'loads/load_mahalla_list.html', {"mahalla":mahalla})

def load_maktab(request):
    tuman_id = request.GET.get('tuman_id')
    maktab = MK.objects.filter(tuman_id=tuman_id).order_by("name")
    return render(request, 'loads/load_maktab_list.html', {"maktab" : maktab})

def load_otm(request):
    vil_id = request.GET.get("viloyat")
    otm = Universitet.objects.filter(viloyat_id=vil_id).order_by("name")
    return render(request, 'loads/load_otm_list.html', {"otm" : otm})



