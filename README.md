# 🏥 HospitalTech

Sistema de gerenciamento hospitalar desenvolvido em Django.  
Inclui módulos de pacientes, triagem, consultas, funcionários, exames, setores, cargos e controle administrativo.  
Ideal para estudos, portfólio e implementação didática.

---

## 📂 Estrutura do Projeto

HospitalTech/
│── hospitalCC/ # App principal do sistema
│── project/ # Configurações gerais do projeto Django
│── manage.py # Arquivo principal de execução
│── admin_default.json # Fixture com usuário padrão


## ⚙️ 1. Como Clonar o Repositório


git clone https://github.com/fernando-s-barreto/hospital-caminho-do-ceu.git
Acesse a pasta do projeto:

🐍 2. Criar e Ativar o Ambiente Virtual
Criar o ambiente:


Copiar código
python -m venv venv

Ativar no PowerShell:
Copiar código
venv\Scripts\Activate.ps1

Ativar no CMD:

Copiar código
venv\Scripts\activate.bat

Se ocorrer erro de permissão:

Copiar código
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser


📦 3. Instalar Dependências

Copiar código
pip install -r requirements.txt

🗂 4. Criar as Tabelas do Banco
Copiar código
python manage.py migrate


👤 5. Carregar Usuário Padrão
Copiar código
python manage.py loaddata admin_default.json

Login padrão:
Login: admin
Senha: admin123

▶️ 6. Rodar o Servidor
Copiar código
python manage.py runserver

Acesse:
http://127.0.0.1:8000/

🛠 7. Solução de Problemas

Erro ao ativar a venv (PowerShell)
Copiar código
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1

Erro ao instalar dependências
Delete a venv:

Copiar código
Remove-Item -Recurse -Force .\venv

Crie novamente:

Copiar código
python -m venv venv

Ative:
Copiar código
venv\Scripts\Activate.ps1

Atualize o pip:
Copiar código
python -m pip install --upgrade pip

Instale dependências:
Copiar código
pip install -r requirements.txt


⚠️ Importante
Nunca envie a pasta venv para o GitHub.

Utilize o arquivo requirements.txt para gerenciar dependências.

📘 Sobre o Projeto
HospitalTech foi desenvolvido como uma aplicação acadêmica para gerenciar processos hospitalares.
Inclui:

Cadastro e consulta de pacientes

Triagem

Agendamento e consultas

Laboratórios

Exames

Funcionários e cargos

Login personalizado com autenticação via Funcionario

Dashboard com estatísticas
