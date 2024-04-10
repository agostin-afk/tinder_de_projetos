from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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
            

class RegisterUpdateForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length= 30,
        min_length= 2,
        required=True,
        help_text='Required.',
        error_messages={
            'min_length': 'please, insert 2 or more characters',
        },
    )
    last_name = forms.CharField(
        max_length= 35,
        min_length=2,
        required= True,
        help_text='Required.',
        error_messages={
            'min_length': 'please, insert 2 or more characters',
        },
    )
    password1 = forms.CharField(
        label='Password',
        strip= True,
        widget= forms.PasswordInput(
            attrs = {'autocomplete': 'new-password'},
        ),
        help_text= password_validation.password_validators_help_text_html(),
        required= False,
    )
    password2 = forms.CharField(
        label= 'Password 2',
        strip= True,
        widget= forms.PasswordInput(
            attrs= {'autocomplete': 'new-password'},
        ),
        help_text = password_validation.password_validators_help_text_html(),
        required= False,
    )
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]
        
    def save(self, commit=True):
        cleaned_data = self.cleaned_data
        user = super().save(commit=False)
        password = cleaned_data.get('password1')
        if password:
            user.set_password(password)
        if commit:
            user.save()
        return user
    def clean(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 != password2:
            self.add_error(
                'password2',
                ValidationError('As senhas não são iguais')
            )
        return super().clean()
    def clean_email(self):
        email = self.cleaned_data.get('email')
        current_email = self.instance.email
        if current_email != email:
            if User.objects.filter(email=email).exists():
                self.add_error('email',
                            ValidationError('Email already exists, try again', code= 'invalid'))
    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if password1:
            try:
                 password_validation.validate_password(password1)
            except ValidationError as errors:
                self.add_error('password1', errors)
        return password1            