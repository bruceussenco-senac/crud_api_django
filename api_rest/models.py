from django.db import models

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    disciplina = models.CharField(max_length=100)

    def __str__(self): return self.nome

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    matricula = models.CharField(max_length=20, unique=True)
    data_nascimento = models.DateField()
    email = models.EmailField(unique=True)

    def __str__(self): return self.nome

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name='cursos')
    alunos = models.ManyToManyField(Aluno, related_name='cursos_matriculados')

    def __str__(self): return self.titulo
