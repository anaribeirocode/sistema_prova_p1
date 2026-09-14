from django.db import models

from categorias.models import Categoria

class Livro(models.Model):
    STATUS_CHOICES = [
        ('Disponivel', 'DISPONIVEL'),
        ('Alugado', 'ALUGADO'),
        ('Reservado', 'RESERVADO'),
    ]

    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    data_publicacao = models.DateField(auto_now=False, auto_now_add=False)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='DISPONIVEL')

    #essa é a chave estrangeira que conecta com os livros e os classifica de acordo com a categoria em que ele se encaixa
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.titulo} ({self.autor})"