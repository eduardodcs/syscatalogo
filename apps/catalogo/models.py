from django.db import models
from datetime import datetime


class Grupo(models.Model):
    nome_grupo = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_grupo

class Produto(models.Model):
    codigo = models.IntegerField()
    nome_produto = models.CharField(max_length=50)
    descricao_produto = models.TextField()
    preco_produto = models.FloatField()
    grupo_produto = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(default=datetime.now, blank=True)
    status_produto = models.BooleanField(default=False)
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
    def __str__(self):
        return self.nome_produto

