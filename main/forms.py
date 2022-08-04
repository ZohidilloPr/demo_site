
from django import forms
from django.urls import reverse_lazy
from .models import Imkonyat, Mahalla, MaktabBitiruvchisi, Maktab

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
            self.fields['mahalla'].queryset = self.instance.maktab.mahalla_set.all() 
            self.fields['maktab'].queryset = self.instance.tuman.maktab_set.all() 