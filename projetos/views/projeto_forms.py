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
 