from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Usuario

class RegistroForm(forms.ModelForm):
    senha1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    senha2 = forms.CharField(label='Confirmação de Senha', widget=forms.PasswordInput)

    class Meta:
        model = Usuario
        fields = ('nome', 'email', 'cpf', 'data_nascimento')

    def clean_senha2(self):
        senha1 = self.cleaned_data.get("senha1")
        senha2 = self.cleaned_data.get("senha2")
        if senha1 and senha2 and senha1 != senha2:
            raise forms.ValidationError("As senhas não coincidem.")
        return senha2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["senha1"])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)