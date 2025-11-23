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

yaml
Copiar código

---

## ⚙️ 1. Como Clonar o Repositório

```bash
git clone https://github.com/fernando-s-barreto/hospital-caminho-do-ceu.git
Acesse a pasta do projeto:

bash
Copiar código
cd HospitalTech
🐍 2. Criar e Ativar o Ambiente Virtual
Criar o ambiente:

bash
Copiar código
python -m venv venv
Ativar no PowerShell:

bash
Copiar código
venv\Scripts\Activate.ps1
Ativar no CMD:

bash
Copiar código
venv\Scripts\activate.bat
Se ocorrer erro de permissão:

bash
Copiar código
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
📦 3. Instalar Dependências
bash
Copiar código
pip install -r requirements.txt
🗂 4. Criar as Tabelas do Banco
bash
Copiar código
python manage.py migrate
👤 5. Carregar Usuário Padrão
bash
Copiar código
python manage.py loaddata admin_default.json
Login padrão:

Login: admin

Senha: admin123

▶️ 6. Rodar o Servidor
bash
Copiar código
python manage.py runserver
Acesse:

cpp
Copiar código
http://127.0.0.1:8000/
🛠 7. Solução de Problemas
Erro ao ativar a venv (PowerShell)
bash
Copiar código
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
venv\Scripts\Activate.ps1
Erro ao instalar dependências
Delete a venv:

bash
Copiar código
Remove-Item -Recurse -Force .\venv
Crie novamente:

bash
Copiar código
python -m venv venv
Ative:

bash
Copiar código
venv\Scripts\Activate.ps1
Atualize o pip:

bash
Copiar código
python -m pip install --upgrade pip
Instale dependências:

bash
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
