# HospitalTech

Este documento explica como instalar, configurar e executar o sistema **HospitalTech**, desenvolvido em Django.

---

## 1. Requisitos

Antes de começar, é necessário ter instalado na máquina:

* Python 3.10 ou superior
* Pip
* Git (opcional)

---

## 2. Baixar o Projeto

Baixe o ZIP da *branch master* do repositório:

```
hospital-tech → Code → Download ZIP
```

Extraia o arquivo.

---

## 3. Criar o Ambiente Virtual

```bash
python -m venv venv
```

Ativar:

* PowerShell:

```bash
venv\Scripts\Activate.ps1
```

* CMD:

```bash
venv\Scripts\activate.bat
```

---

## 4. Instalar Dependências

```bash
pip install -r requirements.txt
```

---

## 5. Aplicar Migrações

```bash
python manage.py migrate
```

---

## 6. Carregar Usuário Padrão (opcional)

```bash
python manage.py loaddata admin_default.json
```

Credenciais:

* Usuário: admin
* Senha: admin123

---

## 7. Executar o Servidor

```bash
python manage.py runserver
```

Acesse:

```
http://127.0.0.1:8000/
```

---

## 8. Estrutura do Projeto

```
hospitalCC/      → App principal
project/         → Configurações do Django
manage.py        → Inicializador
requirements.txt → Dependências
README.md        → Documentação
```

---

## 9. Funcionalidades

* Cadastro e consulta de pacientes
* Triagem
* Consultas e marcações
* Funcionários, cargos e setores
* Exames e laboratórios
* Login via Funcionário
* Dashboard

---

## 10. Problemas Comuns

**"ModuleNotFoundError: No module named 'django'"**
→ Ambiente virtual não ativado ou dependências não instaladas.

**"Could not open requirements.txt"**
→ ZIP baixado da branch errada.

---

## 11. Encerrar

Para parar o servidor:

```
CTRL + C
```

Desativar venv:

```
deactivate
```
