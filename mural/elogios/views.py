from django.shortcuts import render, redirect, get_object_or_404
from .models import Elogio
from .forms import ElogioForm

def lista_elogios(request):
    elogios = Elogio.objects.all()
    return render(request, 'elogios/lista_elogios.html', {'elogios': elogios})

def adicionar_elogio(request):
    if request.method == 'POST':
        form = ElogioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_elogios')
    else:
        form = ElogioForm()
    return render(request, 'elogios/adicionar_elogio.html', {'form': form})

def excluir_elogio(request, id):
    elogio = get_object_or_404(Elogio, id=id)
    elogio.delete()
    return redirect('lista_elogios')  # Redireciona após excluir
