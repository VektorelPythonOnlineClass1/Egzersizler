from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from mainweb.forms import ContactForm, LoginForm, RegisterForm


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RegisterForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password_first = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password_again = forms.CharField(label="Confirm password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean(self):
        cleaned_data = self.cleaned_data
        password_one = self.cleaned_data.get('password_first')
        password_two = self.cleaned_data.get('password_again')
        if password_one != password_two:
            raise forms.ValidationError("Passwords don't match")
        return cleaned_data

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("The username you've chosen is unavailable.")
        return username

    def clean_email(self):
        email_address = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email_address)
        if qs.exists():
            raise forms.ValidationError("The email address you've chosen is already registered.")
        return email_address
    
    
    def login_page(self, request):
        form = LoginForm(request.POST or None)
        context = {
            'form': form
        }
        print(request.user.is_authenticated)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                print("error.......")

        return render(request, "auth/login.html", context=context)

def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,
    }
    if form.is_valid():
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password_first")
        new_user = User.objects.create_user(username, email, password)
    return render(request, "auth/register.html", context=context)

def logout_page(request):
    logout(request)
    return redirect('/')
