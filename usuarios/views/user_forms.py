from django.shortcuts import render, redirect
from projetos.forms import RegisterForm # , RegisterUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required


def login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)
        if form.is_valid():
            user = form.get_user()
            messages.success(request, 'Login successful')
            auth.login(request, user)
            print('dale papai'*4)
            return redirect('projetos:projetos')
        messages.error(request, 'Login inválido')
    return render(
        request,
        'usuarios/login.html',
        {
            'form' : form,
        }
    )