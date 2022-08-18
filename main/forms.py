from django import forms
from .widget import DatePicker
from django.urls import reverse_lazy

from .models import (
    Kollej,
    Maktab, 
    Mahalla, 
    Imkonyat, 
    Universitet,
    KollejBitiruvchisi, 
    MaktabBitiruvchisi, 
    UniversitetBitiruvchisi,
)

imk = Imkonyat.objects.all()

class MaktabForm(forms.ModelForm):
    class Meta:
        model = MaktabBitiruvchisi
        fields = '__all__'

        widgets = {
            'f_name': forms.TextInput(attrs={
                'class':'form-control w-50',
                'placeholder':'Akmal Berdiev Murod o\'g\'li'
            }),
            'img': forms.FileInput(attrs={
                'display':"none"
            }),
            'tuman_mk':forms.Select(attrs={
                'id':'tuman_mk',
                'class':'form-select',
            }),
            'tuman':forms.Select(attrs={
                'class':'form-select',
            }),
            'uy':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Guldiyor ko\'chasi 204uy'
            }),
            'mahalla': forms.Select(attrs={
                "id":"mahalla",
                'class':'form-select',
                'mahalla-queries-url':reverse_lazy("ALM"),
            }),
            'maktab': forms.Select(attrs={
                "id":"maktab",
                'class':'form-select',
                'maktab-queries-url':reverse_lazy("ALMa"),
            }),
            'imkonyat':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'qiziqish':forms.Select(attrs={
                'class':'form-control',
            }),
            'chettili':forms.CheckboxSelectMultiple(),
            't_sana': forms.SelectDateWidget(attrs={
                'id':"datepicker",
                'class':'form-control'
            },years=range(1950, 2023)),
            'phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'332300701'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'example@domain.com'
            }),
            'sport':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'chettili':forms.SelectMultiple(attrs={
                "class":'form-control',
            }),
            'idea':forms.Select(attrs={
                'class':'form-control',
            }),
            'short_f':forms.TextInput(attrs={
                'placeholder':"Misol: 'ishlab chiqarish'",
                'class':'form-control'
            }),
            'univer_sity':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Toshkent axborot texnologiyalar universiteti'
            }),
            'jins':forms.Select(attrs={
                'class':'form-select'
            })

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        self.fields['maktab'].queryset = Maktab.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
                # self.fields['maktab'].queryset = Maktab.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all() 
            # self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all() 
        
        if 'tuman_mk' in self.data:
            try:
                tuman_id = int(self.data.get('tuman_mk'))
                self.fields['maktab'].queryset = Maktab.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all()


class KollejForm(forms.ModelForm):
    class Meta:
        model = KollejBitiruvchisi
        fields = '__all__'

        widgets = {
            'f_name': forms.TextInput(attrs={
                'class':'form-control w-50',
                'placeholder':'Akmal Berdiev Murod o\'g\'li'
            }),
            'img': forms.FileInput(attrs={
                'display':"none"
            }),
            'tuman_mk':forms.Select(attrs={
                'id':'tuman_mk',
                'class':'form-select',
            }),
            'tuman':forms.Select(attrs={
                'class':'form-select',
            }),
            'uy':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Guldiyor ko\'chasi 204uy'
            }),
            'mahalla': forms.Select(attrs={
                "id":"mahalla",
                'class':'form-select',
                'mahalla-queries-url':reverse_lazy("ALM"),
            }),
            'maktab': forms.Select(attrs={
                "id":"maktab",
                'class':'form-select',
                'maktab-queries-url':reverse_lazy("ALMa"),
            }),
            'imkonyat':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'qiziqish':forms.Select(attrs={
                'class':'form-control',
            }),
            'chettili':forms.CheckboxSelectMultiple(),
            't_sana': forms.SelectDateWidget(attrs={
                'id':"datepicker",
                'class':'form-control'
            },years=range(1950, 2023)),
            'phone':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'332300701'
            }),
            'email':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'example@domain.com'
            }),
            'sport':forms.SelectMultiple(attrs={
                'class':'form-control',
            }),
            'chettili':forms.SelectMultiple(attrs={
                "class":'form-control',
            }),
            'idea':forms.Select(attrs={
                'class':'form-control',
            }),
            'short_f':forms.TextInput(attrs={
                'placeholder':"Misol: 'ishlab chiqarish'",
                'class':'form-control'
            }),
            'univer_sity':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Toshkent axborot texnologiyalar universiteti'
            }),
            'guvohnoma':forms.Select(attrs={
                'class':'form-select',
            }),
            'tuman_kj': forms.Select(attrs={
                'class':'form-select',
            }),
            'kollej':forms.Select(attrs={
                'class':'form-select',
            }),
            'stu_way':forms.TextInput(attrs={
                'class':'form-control',
                'placeholder':'Kompyuter injenering',
            }),
            'type':forms.Select(attrs={
                'class':'form-select',    
            }),
            'maqsad':forms.Select(attrs={
                'class':'form-select'
            }),
            'jins':forms.Select(attrs={
                'class':'form-select'
            })

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        # self.fields['kollej'].queryset = Kollej.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get("tuman"))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
                # self.fields['kollej'].queryset = Kollej.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all()
            # self.fields['kollej'].queryset = self.instance.tuman.kollej_set.all()
        
class UniversitetForm(forms.ModelForm):
    class Meta:
        model = UniversitetBitiruvchisi
        fields = '__all__'

        widgets = {
            'mahalla': forms.Select(attrs={
                'id':'mahalla',
                'mahalla-queries-url':reverse_lazy("ALM")
            }),
            'universitet':forms.Select(attrs={
                'id':'universitet',
                # 'universitet-queries-url': reverse_lazy("ALK"),
            }),
            'imkonyat':forms.CheckboxSelectMultiple(),
            'qiziqish':forms.Select(),
            'chettili':forms.CheckboxSelectMultiple(),
            # 't_sana':DatePicker(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get("tuman"))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all()

class MaktabFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        self.fields['maktab'].queryset = Maktab.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
                self.fields['maktab'].queryset = Maktab.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass


class KollejFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass

class UniversiterFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get("tuman"))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
            except (ValueError, TypeError):
                pass

class MaktabNameForm(forms.ModelForm):
    class Meta:
        model = Maktab
        fields = '__all__'

        # widgets = {
        #     'status': forms.TextInput(attrs={
        #         'hidden': 'true'
        #     })
        # }

class KollejNameForm(forms.ModelForm):
    class Meta:
        model = Kollej
        fields = '__all__'

class UniversitetNameForm(forms.ModelForm):
    class Meta:
        model = Universitet
        fields = '__all__'