from django.db import models

class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Topico(models.Model):
    nome = models.CharField(max_length=100)
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nome