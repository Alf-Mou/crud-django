from .model import Usuario, Pessoa
from django.http import HttpResponse
from django.shortcuts import render

# Home da página
def home(request):
    return render(request, "home.html")
 

# Post -> Create
def criar_usuario(request):
    if request.method == "GET":
        return render(request, "cadastra.html")

    elif request.method == "POST":
        print(request.POST)
        post=request.POST

        user = Usuario.objects.create(
            login=post.get("login"),
            senha=post.get("senha")
        )
        user.save()

        pessoa = Pessoa.objects.create(
            nome=post.get("nome"),
            idade=post.get("idade"),
            cpf=post.get("cpf"),
            usuario=user
        )
        pessoa.save()

        return HttpResponse(status=201)
    
    return HttpResponse(status=405)


