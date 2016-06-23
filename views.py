from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from .forms import EstudianteForm
from django.contrib.auth.models import User

def casita(request):
    template = 'index.html'
    return render(request, template)

class formi(View):
    def get(self, request):
        template = 'formi.html'
        form = EstudianteForm()
        context = {
            'form': form
        }
        return render(request, template, context)

    def post(self, request):
        form = EstudianteForm(request.POST, request.FILES)
        username=request.POST.get('nombre')
        password=request.POST.get('boleta')
        if form.is_valid():
            user=User.objects.create_user(username=username,password=password)
            user.save()
            cosa = form.save(commit=False)
            cosa.save()
            return redirect('/proyecto/casi')
        else:
            return redirect('/proyecto/error')

class loggeate(View):
    def get(self, request):
        template_name = 'login.html'
        return render(request, template_name)

    def post(self, request):
        username = request.POST.get('usuario')
        password = request.POST.get('boleta')
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        login(request, user)

        return redirect('/proyecto/logeado')

def logeado(request):
    template = 'logeado.html'
    return render(request,template)

def loggout(request):
    logout(request)
    template = 'logeado.html'
    return render(request,template)
