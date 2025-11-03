from django.shortcuts import render, redirect
from .forms import *

def home(request):
    return render(request, 'home.html')

def cadastrar_paciente(request):
    titulo = 'Paciente'
    if request.method == "POST":
        form = PacienteForm(request.POST)
        message = 'Paciente não foi cadastrado!'
        try:
            form.save()
            message = 'Paciente cadastrada.'
            return render(request, 'cadastrarBase.html', {'form': form, 'message' : message, 'titulo' : titulo})
        except Exception as e:
            message = e
            return render(request, 'cadastrarBase.html', {'form': form, 'message' : message, 'titulo' : titulo})
    form = PacienteForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message' : '', 'titulo' : titulo})

def cadastrar_triagem(request):
    titulo = 'Triagem'
    if request.method == "POST":
        form = TriagemForm(request.POST)
        try:
            form.save()
            message = 'Triagem cadastrada.'
            return render(request, 'cadastrarBase.html', {'form': form, 'message' : message, 'titulo' : titulo})
        except Exception as e:
            print(e)
            return render(request, 'cadastrarBase.html', {'form': form, 'message' : message, 'titulo' : titulo})
    form = TriagemForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message' : '', 'titulo' : titulo})

def cadastrar_funcionario(request):
    titulo = 'Funcionario'
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        message = 'Funcionário não foi cadastrado!'
        try:
            form.save()
            message = 'Funcionário cadastrado.'
            return render(request, 'cadastrarBase.html', {'form': form, 'message' : message, 'titulo' : titulo})
        except Exception as e:
            message = e
            return render(request, 'cadastrarBase.html', {'form': form, 'message' : message, 'titulo' : titulo})
    form = FuncionarioForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message' : '', 'titulo' : titulo})

def cadastrar_cargo(request):
    titulo = 'Cargo'
    if request.method == "POST":
        form = CargoForm(request.POST)
        try:
            form.save()
            message = 'Cargo cadastrado.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = CargoForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def cadastrar_setor(request):
    titulo = 'Setor'
    if request.method == "POST":
        form = SetorForm(request.POST)
        try:
            form.save()
            message = 'Setor cadastrado.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = SetorForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def cadastrar_recepcao(request):
    titulo = 'Recepção'
    if request.method == "POST":
        form = RecepcaoFuncionarioPacienteForm(request.POST)
        try:
            form.save()
            message = 'Recepção cadastrada.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = RecepcaoFuncionarioPacienteForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def cadastrar_consulta(request):
    titulo = 'Consulta'
    if request.method == "POST":
        form = ConsultaMedicoPacienteForm(request.POST)
        try:
            form.save()
            message = 'Consulta cadastrada.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = ConsultaMedicoPacienteForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def cadastrar_marcacao(request):
    titulo = 'Marcar Consulta'
    if request.method == "POST":
        form = MarcarConsultaForm(request.POST)
        try:
            form.save()
            message = 'Consulta marcada.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = MarcarConsultaForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def cadastrar_laboratorio(request):
    titulo = 'Laboratório'
    if request.method == "POST":
        form = LaboratorioForm(request.POST)
        try:
            form.save()
            message = 'Laboratório cadastrado.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = LaboratorioForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def cadastrar_exame(request):
    titulo = 'Exame'
    if request.method == "POST":
        form = ExameForm(request.POST)
        try:
            form.save()
            message = 'Exame cadastrado.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = ExameForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def cadastrar_exame_paciente(request):
    titulo = 'Exame do Paciente'
    if request.method == "POST":
        form = ExamePacienteForm(request.POST)
        try:
            form.save()
            message = 'Exame do paciente cadastrado.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})
    form = ExamePacienteForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})

def consultar_paciente(request):
    dados = Paciente.objects.all()
    return render(request, 'consultar\paciente.html', {'dados': dados})

def consultar_funcionario(request):
    dados = Funcionario.objects.select_related('cargo').all()
    return render(request, 'consultar/funcionario.html', {'dados': dados})

def consultar_triagem(request):
    dados = Triagem_medico_paciente.objects.select_related('funcionario', 'paciente').all()
    return render(request, 'consultar/triagem.html', {'dados': dados})

def consultar_consulta(request):
    dados = Consulta_medico_paciente.objects.select_related('funcionario', 'paciente').all()
    return render(request, 'consultar/consulta.html', {'dados': dados})

def consultar_cargo(request):
    dados = Cargo.objects.all()
    return render(request, 'consultar/cargo.html', {'dados': dados})

def consultar_setor(request):
    dados = Setor.objects.all()
    return render(request, 'consultar/setor.html', {'dados': dados})

def consultar_recepcao(request):
    dados = Recepcao_funcionario_paciente.objects.select_related('funcionario', 'paciente', 'setor').all()
    return render(request, 'consultar/recepcao.html', {'dados': dados})

def consultar_marcacao(request):
    dados = Marcar_consulta.objects.select_related('funcionario', 'paciente').all()
    return render(request, 'consultar/marcacao.html', {'dados': dados})

def consultar_laboratorio(request):
    dados = Laboratorio.objects.all()
    return render(request, 'consultar/laboratorio.html', {'dados': dados})

def consultar_exame(request):
    dados = Exame.objects.select_related('laboratorio').all()
    return render(request, 'consultar/exame.html', {'dados': dados})

def consultar_exame_paciente(request):
    dados = Exame_paciente.objects.select_related('paciente', 'exame').all()
    return render(request, 'consultar/exame_paciente.html', {'dados': dados})