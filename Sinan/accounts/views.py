from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model

from mainweb.forms import ContactForm, LoginForm, RegisterForm

User = get_user_model()

def home_page(request):
    return render(request, 'base.html',context={})

def about_page(request):
    return render(request, 'about.html',context={})

def contact_page(request):
    contact_form = contact_form(request.POST or None)
    context = {
        'title':'Contact Us',
        'form': contact_form,             
        
    }
    
    if contact_form.is_valid():
        print('FORM IS VALID')
        print(contanct_form.cleaned_data)
        return redirect('/contact')
        
    return render(request, 'base.html',context={})

def login_page(request):
    form = LoginForm(request.POST or None)
    context = {'form': form            
}
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        User = authenticate(request, username=username, password=password)
    if User is not None:
        login(request, User)
        return redirect('/')
    else:
        print("HATA.......")
        return render(request, "auth/login.html", context=context)


def register_page (request):
    form = RegisterForm(request.POST or None)
    context = {
        'form': form,       
}
    
    if form.is_valid():
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email')    
        password = form.cleaned_data.get('password_first')
        User = User.objects.create_user(username, email, password)
        
    return render(request, "auth/register.html", context=context)

def logout_page(request):
    logout(request)
    return redirect('/')
