from django.forms import ModelForm
from .models import MdContratosDiario


class MdContratosDiarioForm(ModelForm):
    class Meta:
        model = MdContratosDiario
        fields = '__all__'
