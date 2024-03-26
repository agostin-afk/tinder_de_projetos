from projetos.models import Projetos
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation


class Projetoforms(forms.ModelForm):
    logo = forms.ImageField(
        widget= forms.FileInput(
            attrs= {
                'accept': 'iamge/*',
            }
        ),
        required= False,
    )
    nome = forms.CharField(
        widget= forms.TextInput(
            attrs= {
                'placeholder': 'Nome do projeto',
            }
        ),
        help_text= 'insira o nome do projeto'
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #self.fields['first_name'].widget.atttr.update({
        #})
    
    class Meta:
        model = Projetos
        fields = (
            'nome',
            'sigla',
            'numero',
            'email_responsavel',
            'descricao',
            'logo',
            'categoria',
                )
    def clean(self):
        #cleaned_data = self.cleaned_data
        msg =  ValidationError(
                'campos inválidos',
                code='invalid'
            )
        return super().clean()

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        required= True,
        min_length= 3,
        )
    last_name = forms.CharField(
        required= True,
        min_length=3,
    )
    email = forms.EmailField()
    class Meta: 
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
            'username',
            'password1',
            'password2',
            
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        
        if User.objects.filter(email=email).exists():
            self.add_error('email',
                           ValidationError('Email already exists, try again', code= 'invalid'))