from django import forms
from myapp.models import Chuvas

class ChuvasForm(forms.ModelForm):
  class Meta:
    model = Chuvas
    fields = ('data', 'volume')
    widgets = {
      'data': forms.TextInput(attrs={'class':'form-control'}),
      'volume': forms.NumberInput(attrs={'class':'form-control'}),
    }
