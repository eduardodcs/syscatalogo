from django.shortcuts import render
from .models import Produto
from usuarios.models import Usuario

def index(request):
    produtos  = Produto.objects.order_by('-data_cadastro').filter(status_produto=True)
    usuarios = Usuario.objects.all()
    dados  = {
        'produtos' : produtos,
        'usuarios' : usuarios
    }
    return render(request, 'index.html', dados)
