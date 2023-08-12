from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import FormView
from main import forms
from .models import Categoria, Produto

class ViewFaleConosco(FormView):
    template_name = "fale_conosco.html"
    form_class = forms.FormFaleConosco
    success_url = "/"

    def form_valid(self, form) -> HttpResponse:
        form.enviar_mensagem_por_email()
        return super().form_valid(form)

def listar_produtos(request, slug_categoria=None):
    categoria = None
    lista_categoria = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(disponivel=True)
    
    for produto in lista_produtos:
        print(produto.get_absolute_url())

    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = Produto.objects.filter(categoria=categoria)


    contexto = {
        "categoria": categoria,
        "lista_categorias": lista_categoria,
        "lista_produtos": lista_produtos,
    }

    return render(request, "produto/listar.html", contexto)

def detalhes_produto(request, slug_produto=None):
    produto = get_object_or_404(Produto, slug=slug_produto, disponivel=True)
    contexto = {"produto": produto,}
    return render(request, "produto/detalhes.html", contexto)