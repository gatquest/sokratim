from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        required=True,
        help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="Пароль:",
        required=True,
        help_text='Пароль не должен быть слишком похож на другую вашу личную информацию. <br> Ваш пароль должен содержать как минимум 8 символов.<br> Пароль не может состоять только из цифр.',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(label="Е-mail:", required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        del self.fields['password2']

class UserUpdateForm(forms.ModelForm):
        username = forms.CharField(
            label="Имя пользователя",
            required=True,
            help_text='Обязательное поле. Не более 150 символов. Только буквы, цифры и символы @/./+/-/_.',
            widget=forms.TextInput(attrs={'class': 'form-control'})
        )
        email = forms.EmailField(label="Е-mail:", required=True)

        class Meta:
            model = User
            fields = ['username', 'email']
