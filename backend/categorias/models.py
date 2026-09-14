from django.db import models

class Categoria(models.Model):
    TIPO_CHOICES = [
        ('Romance', 'ROMANCE'),
        ('Aventura', 'AVENTURA'),
        ('Ação', 'AÇÃO'),
        ('Fantasia', 'FANTASIA'),
        ('Terror', 'TERROR'),
        ('Clássicos', 'CLÁSSICOS'),
    ]

    nome = models.CharField(max_length=100, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return f"{self.nome} ({self.descricao})"