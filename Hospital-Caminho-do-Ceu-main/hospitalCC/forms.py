from django import forms
from .models import *

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'
        widgets = {
            'CPF': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'nome': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'data_nasc': forms.DateInput(attrs={'type': 'date', 'class': 'form-main input-main'}),
            'endereco': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'tel_paciente': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'tel_responsavel': forms.TextInput(attrs={'class': 'form-main input-main'}),
        }

class TriagemForm(forms.ModelForm):
    class Meta:
        model = Triagem_medico_paciente
        fields = '__all__'
        widgets = {
            'funcionario': forms.Select(attrs={'class': 'form-main select-main'}),
            'paciente': forms.Select(attrs={'class': 'form-main select-main'}),
            'altura': forms.NumberInput(attrs={'class': 'form-main input-main', 'step': '0.01'}),
            'peso': forms.NumberInput(attrs={'class': 'form-main input-main', 'step': '0.01'}),
            'temperatura': forms.NumberInput(attrs={'class': 'form-main input-main', 'step': '0.1'}),
            'pressao_sistolica': forms.NumberInput(attrs={'class': 'form-main input-main'}),
            'pressao_diastolica': forms.NumberInput(attrs={'class': 'form-main input-main'}),
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-main input-main'}),
        }

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'is_medico': forms.CheckboxInput(attrs={'class': 'form-main checkbox-main'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-main input-main'}),
            'cargo': forms.Select(attrs={'class': 'form-main select-main'}),
        }

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-main input-main'}),
        }

class SetorForm(forms.ModelForm):
    class Meta:
        model = Setor
        fields = '__all__'
        widgets = {
            'setor': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'descricao': forms.Textarea(attrs={'class': 'form-main textarea-main'}),
        }

class RecepcaoFuncionarioPacienteForm(forms.ModelForm):
    class Meta:
        model = Recepcao_funcionario_paciente
        fields = '__all__'
        widgets = {
            'funcionario': forms.Select(attrs={'class': 'form-main select-main'}),
            'paciente': forms.Select(attrs={'class': 'form-main select-main'}),
            'setor': forms.Select(attrs={'class': 'form-main select-main'}),
        }

class ConsultaMedicoPacienteForm(forms.ModelForm):
    class Meta:
        model = Consulta_medico_paciente
        fields = '__all__'
        widgets = {
            'funcionario': forms.Select(attrs={'class': 'form-main select-main'}),
            'paciente': forms.Select(attrs={'class': 'form-main select-main'}),
            'sintomas': forms.Textarea(attrs={'class': 'form-main textarea-main'}),
            'prescricao_medica': forms.Textarea(attrs={'class': 'form-main textarea-main'}),
            'doenca': forms.TextInput(attrs={'class': 'form-main input-main'}),
        }

class MarcarConsultaForm(forms.ModelForm):
    class Meta:
        model = Marcar_consulta
        fields = '__all__'
        widgets = {
            'funcionario': forms.Select(attrs={'class': 'form-main select-main'}),
            'paciente': forms.Select(attrs={'class': 'form-main select-main'}),
            'data_hora_consulta': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-main input-main'}),
        }

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'endereco': forms.TextInput(attrs={'class': 'form-main input-main'}),
        }

class ExameForm(forms.ModelForm):
    class Meta:
        model = Exame
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-main input-main'}),
            'laboratorio': forms.Select(attrs={'class': 'form-main select-main'}),
        }

class ExamePacienteForm(forms.ModelForm):
    class Meta:
        model = Exame_paciente
        fields = '__all__'
        widgets = {
            'paciente': forms.Select(attrs={'class': 'form-main select-main'}),
            'exame': forms.Select(attrs={'class': 'form-main select-main'}),
            'data_hora_retirada': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-main input-main'}),
        }