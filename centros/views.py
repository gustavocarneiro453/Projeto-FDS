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

@login_required
def remover_centros(request, centro_id):
    try:
        centro = CentroColeta.objects.get(id=centro_id, usuario_responsavel=request.user)
        if request.method == 'POST':
            centro.delete()
            return redirect('centros:lista_centros')
    except CentroColeta.DoesNotExist:
        return render(request, 'centros/centro_nao_encontrado.html')
    return render(request, 'centros/remover_centro.html', {'centro': centro})         