from django.forms import ModelForm
from .models import Ativo, Colaborador

class AtivoForm(ModelForm):
    class Meta:
        model = Ativo
        fields = ['mac', 'dev_name', 'ports', 'poe', 'ipv4', 'ipv6', 'serial', 'patrimonio',
                  'instalado', 'local', 'rack_pos', 'instaladores']

class ColabForm(ModelForm):
    class Meta:
        model = Colaborador
        fields = ['colab_name', 'telefone', 'celular', 'email']