from django.shortcuts import get_object_or_404,render,redirect
from django.forms.models import inlineformset_factory
from django.contrib import messages
from .models import Profile, Meep
from .forms import MeepForm, SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import Q


def home_in(request):
    if request.user.is_authenticated:
       form = MeepForm(request.POST or None)
       if request.method == "POST":
            if form.is_valid():
                meep = form.save(commit=False)
                meep.user =request.user
                meep.save()
                messages.success(request, ("Ingresado!!"))
                return render(request, 'home.html', {})
       meeps = Meep.objects.all().order_by("-created_at")
       return render(request, 'home_in.html', {"meeps":meeps, "form":form})
    else:
         messages.success(request, ("Tenes que estar logueado"))
         return render(request, 'home_in.html', {"meeps":meeps})


def home(request):
    if request.user.is_authenticated:
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'home.html', {"meeps":meeps})

    else:
         messages.success(request, ("Tenes que estar logueado"))
         return render(request, 'home.html', {})

    


def profile_list(request):
    if request.user.is_authenticated:
        profiles = Profile.objects.exclude(user=request.user)
        return render(request, 'profile_list.html', {"profiles":profiles})
    else:
        messages.success(request, ("Tenes que estar logueado"))
        #return redirect('home.html') 
        return render(request, 'home.html', {})
    

def profile(request, pk):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user_id=pk)
        meeps = Meep.objects.filter(user_id=pk).order_by("-created_at")

        if request.method == "POST":
           current_user_profile = request.user.profile
           action = request.POST['follow']

           if action == "unfollow":
               current_user_profile.follows.remove(profile)
           elif action == "follow":
               current_user_profile.follows.add(profile)

           current_user_profile.save()   


        return render(request, "profile.html", {"profile":profile, "meeps":meeps})
    else:
        messages.success(request, ("Tenes que estar logueado"))
        #return redirect('home.html') 
        return render(request, 'home.html', {})
    
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("Te has Logueado.."))
            return render(request, 'home.html', {})
        else:
            messages.success(request, ("Hubo un error, por favor trate de nuevo.."))
            return render(request, 'login.html', {})   

    return render(request, "login.html", {"login":login})

def logout_user(request):
    logout(request)
    messages.success(request, ("Has salido de tu Usuario.."))
    return render(request, 'home.html', {})

def register_user(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            #first_name = form.cleaned_data['first_name']
            #last_name = form.cleaned_data['last_name']
            #email = form.cleaned_data['email']

            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Te Registrastes.."))
            return render(request, 'home.html', {})
    return render(request, 'register.html', { 'form':form })


def edit_meep(request, pk):
    if request.user.is_authenticated:
        meep = get_object_or_404(Meep, id=pk)
        if request.user.username == meep.user.username:
            
            form = MeepForm(request.POST or None, instance=meep)
            if request.method == "POST":
                if form.is_valid():
                    meep = form.save(commit=False)
                    meep.user =request.user
                    meep.save()
                    messages.success(request, ("Actualizado!!"))
                    return render(request, 'home.html', {})

            else:
                return render(request, "edit_meep.html", {'form':form, 'meep':meep})
        else:
            messages.success(request, ("No hicistes esto.."))
            return render(request, 'home.html', {})
    else:
         messages.success(request, ("Necesitas loguearte para continuar.."))
         return render(request, 'home.html', {})

def search(request):
    if request.method == "POST":
        search = request.POST['search']
        searched = Meep.objects.filter(domicilio__contains=search) 
        
        return render(request, 'search.html', {'search':search, 'searched':searched })       
    else: 
        return render(request, 'search.html', {})  


def listados(request):
    if request.user.is_authenticated:
        meeps = Meep.objects.all().order_by("-created_at")
        return render(request, 'listados.html', {"meeps":meeps})

    else:
         messages.success(request, ("Tenes que estar logueado"))
         return render(request, 'listados.html', {})    

# Create your views here.
