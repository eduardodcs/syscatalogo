from .models import Usuario
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import auth, messages


def campo_vazio(campo):
    return not campo.strip()

def senhas_nao_sao_iguais(senha, senha2):
    return senha != senha2

def links_catalogo():
    usuarios = Usuario.objects.all()
    dados = {
        'usuarios': usuarios
    }
    return dados

def catalogo(request, usuario):
    dados_usuario = get_object_or_404(Usuario, username=usuario)
    usuarios = Usuario.objects.all()
    usuario_exibir = {
        'dados' : dados_usuario,
        'usuarios' : usuarios,
    }
    return render(request, 'catalogo.html', usuario_exibir)

def login(request):
    if request.method == ('POST'):
        usuario = request.POST['usuario']
        senha = request.POST['senha']
        if campo_vazio(usuario) or campo_vazio(senha):
            messages.error(request, "Os campos Email e Senha não podem ficar em branco")
            return redirect('login')
        if Usuario.objects.filter(username=usuario).exists():
            user = auth.authenticate(request, username=usuario, password=senha)
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    catalogos = links_catalogo()
    return render(request, 'login.html', catalogos)

def cadastro_usuario(request):
    if request.method == 'POST':
        usuario = request.POST['nome_usuario']
        email = request.POST['email']
        senha = request.POST['senha']
        senha2 = request.POST['senha2']
        if campo_vazio(usuario):
            messages.error(request, 'O campo usuario não pode ficar em branco.')
            return redirect('cadatro_usuario')
        if campo_vazio(email):
            messages.error(request, 'O campo email não pode ficar em branco.')
            return redirect('cadatro_usuario')
        if campo_vazio(senha):
            messages.error(request, 'O campo senha não pode ficar em branco.')
            return redirect('cadatro_usuario')
        if Usuario.objects.filter(username=usuario).exists():
            messages.error(request, 'Usuário já existe.')
            return redirect('cadatro_usuario')
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Email já cadastrado.')
            return redirect('cadatro_usuario')
        if senhas_nao_sao_iguais(senha, senha2):
            messages.error(request, 'As senhas são iguais.')
            return redirect('cadatro_usuario')
        user = Usuario.objects.create_user(username=usuario, email=email, password=senha)
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso')
        return redirect('login')
    catalogos = links_catalogo()
    return render(request, 'cadastro_usuario.html', catalogos)

def dashboard(request):
    if request.user.is_authenticated:
        catalogos = links_catalogo()
        return render(request, 'dashboard.html', catalogos)
    else:
        return redirect('index')

