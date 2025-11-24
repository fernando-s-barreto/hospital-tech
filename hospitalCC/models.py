from django.db import models
from django.contrib.auth.hashers import make_password


class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nome


class Funcionario(models.Model):
    id_func = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    login = models.CharField(max_length=50, unique=True)
    is_medico = models.BooleanField(default=False)
    senha = models.CharField(max_length=128)
    cargo = models.ForeignKey(Cargo, on_delete=models.PROTECT)

    def save(self, *args, **kwargs):
        if not self.senha.startswith('pbkdf2_'):
            self.senha = make_password(self.senha)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nome


class Paciente(models.Model):
    CPF = models.CharField(max_length=11, primary_key=True)
    nome = models.CharField(max_length=100)
    data_nasc = models.DateField()
    endereco = models.CharField(max_length=255)
    tel_paciente = models.CharField(max_length=15)
    tel_responsavel = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Setor(models.Model):
    id_setor = models.AutoField(primary_key=True)
    setor = models.CharField(max_length=50)
    descricao = models.TextField(null=True)

    def __str__(self):
        return self.setor


class Recepcao_funcionario_paciente(models.Model):
    id_recepcao = models.AutoField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    data_hora = models.DateTimeField(auto_now_add=True)
    setor = models.ForeignKey(Setor, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.paciente}.{self.funcionario}.{self.data_hora}.{self.setor}.'


class Triagem_medico_paciente(models.Model):
    id_triagem = models.AutoField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    altura = models.FloatField()
    peso = models.FloatField()
    temperatura = models.FloatField()
    pressao_sistolica = models.IntegerField()
    pressao_diastolica = models.IntegerField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.paciente}-{self.data_hora}'


class Consulta_medico_paciente(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    sintomas = models.TextField()
    prescricao_medica = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)
    doenca = models.CharField(max_length=100, blank=True)


class Marcar_consulta(models.Model):
    id_marcacao = models.AutoField(primary_key=True)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.PROTECT)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    data_hora_marcacao = models.DateTimeField(auto_now_add=True)
    data_hora_consulta = models.DateTimeField()


class Laboratorio(models.Model):
    id_laboratorio = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id_laboratorio}-{self.nome}'


class Exame(models.Model):
    id_exame = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome



class Exame_paciente(models.Model):
    id_exame_paciente = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.PROTECT)
    exame = models.ForeignKey(Exame, on_delete=models.PROTECT)
    data_hora_realizacao = models.DateTimeField(auto_now_add=True)
    data_hora_retirada = models.DateTimeField(null=True)
