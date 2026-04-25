from django import forms

from .models import Bitik, Savol


class SavolForm(forms.ModelForm):
    class Meta:
        model = Savol
        fields = ['sinf', 'savol', 'variant1', 'variant2', 'variant3', 'tjavob', 'image']
        labels = {
            'sinf': 'Sinf',
            'savol': 'Savol matni',
            'variant1': 'Variant A',
            'variant2': 'Variant B',
            'variant3': 'Variant C',
            'tjavob': "To'g'ri javob",
            'image': 'Rasm (ixtiyoriy)',
        }


class BitikForm(forms.ModelForm):
    class Meta:
        model = Bitik
        fields = ['matn', 'muallif']
        labels = {
            'matn': 'Iqtibos matni',
            'muallif': 'Muallif',
        }
