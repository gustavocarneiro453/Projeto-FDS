from django.shortcuts import render, redirect
from .forms import CentroColetaForm
from django.contrib.auth.decorators import login_required
from .models import CentroColeta

@login_required
def cadastrar_centro(request):
    if request.method == 'POST':
        form = CentroColetaForm(request.POST)
        if form.is_valid():
            centro = form.save(commit=False)
            centro.usuario_responsavel = request.user  # Associa o centro ao usuario autenticado
            centro.save()
            return redirect('centros:lista_centros')  # Redirecionar para a lista de centros
    else:
        form = CentroColetaForm()
    return render(request, 'centros/cadastrar_centro.html', {'form': form})

def lista_centros(request):
    centros = CentroColeta.objects.all() 
    return render(request, 'centros/lista_centros.html', {'centros': centros})