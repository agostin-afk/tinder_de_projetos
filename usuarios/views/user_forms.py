from django.shortcuts import render, redirect
from usuarios.forms import RegisterForm, RegisterUpdateForm
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
    
def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário registrado")
            return redirect('contact:index')
    return render(
        request,
        'usuarios/register.html',
        {
            'form': form,
        },
    )

def logout(request):
    auth.logout(request)
    return redirect('usuarios:login')

def update_user(request):
    form = RegisterUpdateForm(instance= request.user)
    if request.method == 'POST':
        form = RegisterUpdateForm(data= request.POST, instance= request.user)
        if form.is_valid():
            form.save()
            return redirect('usuarios:login')
    return render(
        request,
        'usuarios/user_update.html',
        {
            'form': form
        }
    )