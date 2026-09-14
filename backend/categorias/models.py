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
    #Serve para indicar quando aquela categoria foi adicionada ao sistema, primoridalmente para visualização administrativa
    data_entrada_sistema = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.nome} ({self.descricao})"