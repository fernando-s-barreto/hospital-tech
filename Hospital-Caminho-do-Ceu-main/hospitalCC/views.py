from django.shortcuts import render, redirect
from django.db.models import Count
from django.db.models.functions import TruncMonth

from .forms import *
from .models import *

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from .models import Funcionario

def login_view(request):
    if request.method == "POST":
        cpf = request.POST.get("cpf")
        senha = request.POST.get("senha")

        try:
            user = Funcionario.objects.get(id_func=cpf)
        except:
            return render(request, "login.html", {"erro": "CPF não encontrado."})

        if check_password(senha, user.senha):
            request.session["usuario_id"] = user.id_func
            request.session["usuario_nome"] = user.nome
            return redirect("home")

        return render(request, "login.html", {"erro": "Senha incorreta."})

    return render(request, "login.html")


def logout_view(request):
    request.session.flush()
    return redirect("login")


def home(request):
    if not request.session.get("usuario_id"):
        return redirect("login")

    pacientes_count = Paciente.objects.count()
    consultas_count = Consulta_medico_paciente.objects.count()
    exames_count = Exame_paciente.objects.count()
    funcionarios_count = Funcionario.objects.count()

    ultimos_pacientes = Paciente.objects.order_by('-CPF')[:5]

    consultas_mes_qs = (
        Consulta_medico_paciente.objects
        .annotate(mes=TruncMonth("data_hora"))
        .values("mes")
        .annotate(total=Count("id_consulta"))
        .order_by("mes")
    )

    meses_labels = [
        c["mes"].strftime("%b/%Y") if c["mes"] else ""
        for c in consultas_mes_qs
    ]
    consultas_por_mes = [c["total"] for c in consultas_mes_qs]

    exames_setor_qs = (
        Exame_paciente.objects
        .values("exame__laboratorio__nome")
        .annotate(total=Count("id_exame_paciente"))
        .order_by("exame__laboratorio__nome")
    )

    setores_labels = [e["exame__laboratorio__nome"] or "" for e in exames_setor_qs]
    exames_por_setor = [e["total"] for e in exames_setor_qs]

    contexto = {
        "pacientes_count": pacientes_count,
        "consultas_count": consultas_count,
        "exames_count": exames_count,
        "funcionarios_count": funcionarios_count,
        "ultimos_pacientes": ultimos_pacientes,
        "meses_labels": meses_labels,
        "consultas_por_mes": consultas_por_mes,
        "setores_labels": setores_labels,
        "exames_por_setor": exames_por_setor,
    }

    return render(request, "home.html", contexto)


# ===============================
# CADASTROS (FORM.SAVE)
# ===============================
def cadastrar_paciente(request):
    titulo = 'Paciente'
    if request.method == "POST":
        form = PacienteForm(request.POST)
        try:
            form.save()
            message = 'Paciente cadastrado.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})

    form = PacienteForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})


def cadastrar_triagem(request):
    titulo = 'Triagem'
    if request.method == "POST":
        form = TriagemForm(request.POST)
        try:
            form.save()
            message = 'Triagem cadastrada.'
        except Exception as e:
            message = str(e)
        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})

    form = TriagemForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})


def cadastrar_funcionario(request):
    titulo = 'Funcionário'
    if request.method == "POST":
        form = FuncionarioForm(request.POST)
        try:
            form.save()
            message = 'Funcionário cadastrado.'
        except Exception as e:
            message = str(e)

        return render(request, 'cadastrarBase.html', {'form': form, 'message': message, 'titulo': titulo})

    form = FuncionarioForm()
    return render(request, 'cadastrarBase.html', {'form': form, 'message': '', 'titulo': titulo})


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
    titulo = 'Marcação'
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


# ===========================================
# CONSULTAS (LISTAGEM)
# ===========================================
def consultar_paciente(request):
    dados = Paciente.objects.all()
    return render(request, 'consultar/paciente.html', {'dados': dados})

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
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CargoForm
from .models import Cargo



