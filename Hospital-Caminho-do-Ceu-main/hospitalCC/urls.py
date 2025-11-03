from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home')
]

# Cadastros
urlpatterns += [
    path('cadastrar-paciente/', cadastrar_paciente, name='cadastrar_paciente'),
    path('cadastrar-triagem/', cadastrar_triagem, name='cadastrar_triagem'),
    path('cadastrar-funcionario/', cadastrar_funcionario, name='cadastrar_funcionario'),
    path('cadastrar-cargo/', cadastrar_cargo, name='cadastrar_cargo'),
    path('cadastrar-setor/', cadastrar_setor, name='cadastrar_setor'),
    path('cadastrar-recepcao/', cadastrar_recepcao, name='cadastrar_recepcao'),
    path('cadastrar-consulta/', cadastrar_consulta, name='cadastrar_consulta'),
    path('cadastrar-marcacao/', cadastrar_marcacao, name='cadastrar_marcacao'),
    path('cadastrar-laboratorio/', cadastrar_laboratorio, name='cadastrar_laboratorio'),
    path('cadastrar-exame/', cadastrar_exame, name='cadastrar_exame'),
    path('cadastrar-exame-paciente/', cadastrar_exame_paciente, name='cadastrar_exame_paciente'),
]

# Consultas
urlpatterns += [
    path('consultar-paciente/', consultar_paciente, name='consultar_paciente'),
    path('consultar-funcionario/', consultar_funcionario, name='consultar_funcionario'),
    path('consultar-triagem/', consultar_triagem, name='consultar_triagem'),
    path('consultar-consulta/', consultar_consulta, name='consultar_consulta'),
    path('consultar-cargo/', consultar_cargo, name='consultar_cargo'),
    path('consultar-setor/', consultar_setor, name='consultar_setor'),
    path('consultar-recepcao/', consultar_recepcao, name='consultar_recepcao'),
    path('consultar-marcacao/', consultar_marcacao, name='consultar_marcacao'),
    path('consultar-laboratorio/', consultar_laboratorio, name='consultar_laboratorio'),
    path('consultar-exame/', consultar_exame, name='consultar_exame'),
    path('consultar-exame-paciente/', consultar_exame_paciente, name='consultar_exame_paciente'),
]