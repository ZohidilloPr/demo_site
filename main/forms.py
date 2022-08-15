
from django import forms
from django.urls import reverse_lazy

from .models import (
    Imkonyat, 
    KollejBitiruvchisi, 
    Mahalla, 
    MaktabBitiruvchisi, 
    Maktab, 
    Kollej,
    Universitet,
    UniversitetBitiruvchisi,
)

imk = Imkonyat.objects.all()

class MaktabForm(forms.ModelForm):
    class Meta:
        model = MaktabBitiruvchisi
        fields = '__all__'

        widgets = {
            'mahalla': forms.Select(attrs={
                "id":"mahalla",
                'mahalla-queries-url':reverse_lazy("ALM"),
            }),
            'maktab': forms.Select(attrs={
                "id":"maktab",
                'maktab-queries-url':reverse_lazy("ALMa"),
            }),
            'imkonyat':forms.CheckboxSelectMultiple(),
            'qiziqish':forms.CheckboxSelectMultiple(),
            'chettili':forms.CheckboxSelectMultiple(),
        }

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
        elif self.instance.pk:
            self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all() 
            self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all() 

class KollejForm(forms.ModelForm):
    class Meta:
        model = KollejBitiruvchisi
        fields = '__all__'

        widgets = {
            'mahalla': forms.Select(attrs={
                'id':'mahalla',
                'mahalla-queries-url':reverse_lazy("ALM")
            }),
            'kollej':forms.Select(attrs={
                'id':'kollej',
                'kollej-queries-url': reverse_lazy("ALK"),
            }),
            'imkonyat':forms.CheckboxSelectMultiple(),
            'qiziqish':forms.CheckboxSelectMultiple(),
            'chettili':forms.CheckboxSelectMultiple(),
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
            'qiziqish':forms.CheckboxSelectMultiple(),
            'chettili':forms.CheckboxSelectMultiple(),
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
        # elif self.instance.pk:
        #     self.fields['mahalla'].queryset = self.instance.tuman.mahalla_set.all()
        #     self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all()

class KollejFilterForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['mahalla'].queryset = Mahalla.objects.none()
        self.fields['kollej'].queryset = Kollej.objects.none()

        if 'tuman' in self.data:
            try:
                tuman_id = int(self.data.get('tuman'))
                self.fields['mahalla'].queryset = Mahalla.objects.filter(tuman_id=tuman_id).all()
                self.fields['kollej'].queryset = Kollej.objects.filter(tuman_id=tuman_id).all()
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