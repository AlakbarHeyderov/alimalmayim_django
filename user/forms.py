from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label = "Istifadeci adi")
    password = forms.CharField(label = "Parolunuz",widget = forms.PasswordInput)
    



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30, label = "Istifadeci adiniz")
    password = forms.CharField(max_length=20, label = "Sifreniz", widget = forms.PasswordInput)
    confirm = forms.CharField(max_length=20, label = "Sifre testiqle", widget = forms.PasswordInput)

    def clean(self):
        usename = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        if password and confirm and password != confirm:
            raise forms.ValidationError("Sifreler uygun gelmir")
        
        values = {
            "username": usename,
            "password": password
        }
        return values