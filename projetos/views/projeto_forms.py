from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from projetos.models import Projetos
from projetos.forms import Projetoforms



def create(request):
    form_action = reverse('projetos:projeto_forms')
    if request.method == 'POST':
        form = Projetoforms(request.POST, request.FILES)
        context = {
            'form': form,
            'form_action': form_action,
        }
        if form.is_valid():
            print('form salvo')
            projeto= form.save(commit=False)
            projeto.criador = request.user
            projeto.save()
            return redirect('projetos:projetos',)
        return render(
            request,
            'projetos/create.html',
            context
        )

    
    context = {
        'form': Projetoforms(),
        'form_action': form_action,   
    }
    return render(
        request,
        'projetos/create.html',
        context
        )


def update(request, projeto_id):
    projeto = get_object_or_404(Projetos, pk= projeto_id, show=True)
    form_action = reverse('projetos:update', args=(projeto_id,))
    
    if request.method == 'POST':
        forms = Projetoforms(request.POST, request.FILES, instance=projeto)
        context={
            'form': forms,
            'form_action': form_action, 
        }
        if forms.is_valid():
            projeto= forms.save()
            return redirect('projetos:update', projeto_id=projeto.pk)
        return render(
            request,
            'projetos/create.html',
            context
            )
    context={
        'form': Projetoforms(instance=projeto),
        'form_action': form_action,
    }
    return render(
        request,
        'projetos/create.html',
        context
    )