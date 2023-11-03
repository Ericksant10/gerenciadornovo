from django.shortcuts import render, redirect, get_object_or_404
from .models import Materia
from .form import MateriaForm, TopicoForm

def materia_lista(request):
    materias = Materia.objects.all()
    form = MateriaForm()
    topico_form = TopicoForm()

    if request.method == 'POST':
        if 'adicionar_materia' in request.POST:
            form = MateriaForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('materia_lista')
            
        elif 'adcionar_topico' in request.POST:
            topico_form = TopicoForm(request.POST)
            if form.is_valid():
                topico_form.save()
                return redirect('mateteira_lista')
    
    return render(request, 'estudos/materia_lista.html', {'materias': materias, 'form':form, 'topico_form':topico_form})

def remover_materia(request, materia_id):
    materia = get_object_or_404(Materia, id=materia_id)

    if request.method == 'POST':
        materia.delete()
        return redirect('materia_lista')
    
    return render(request, 'estudos/remover_materia.html', {'materia':materia})
