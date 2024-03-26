from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.paginator import Paginator
from projetos.models import Projetos

def projetos(request):
    contacts = Projetos.objects.filter(show=True)
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'site_title': 'Projetos -',
    }
    return render(
        request,
        'projetos/index.html',
        context
        )
