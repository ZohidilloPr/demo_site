from django.shortcuts import render

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