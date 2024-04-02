from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from projetos.models import Projetos
from projetos.forms import Projetoforms


def projeto_single(request, projeto_id):
    single_projeto = get_object_or_404(Projetos, pk= projeto_id, show=True)

    context = {
        'projeto': single_projeto,
    }
    return render(
        request,
        'projetos/single_projeto.html',
        context
        )
