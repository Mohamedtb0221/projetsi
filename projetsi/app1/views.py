from django.contrib import messages
from django.shortcuts import render,redirect,HttpResponse
from app1.filters import *


from .models import *
from .forms import *

# Create your views here.

def ajout_officier(request):
    if request.method == 'POST':
        form = officierForm(request.POST)
        if form.is_valid():
            form.save()
            form = officierForm()
            mssg = "officier ajouté, vous pouvez ajouté une autre"

            return render(request, "ajoutOfficier.html", {"form": form, "message": mssg})
    else:
        form = officierForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutOfficier.html", {"form": form, "message ": mssg})

def ajout_naissance(request):
    if request.method == 'POST':
        form = naissanceForm(request.POST)
        if form.is_valid():
            form.save()
            form = naissanceForm()
            mssg = "act ajouté, vous pouvez ajouté une autre"
            return render(request, "ajoutNaissance.html", {"form": form, "message": mssg})
    else:
        form = naissanceForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutNaissance.html", {"form": form, "message ": mssg})

def ajout_mariage(request):
    if request.method == 'POST':
        form = mariageForm(request.POST)
        if form.is_valid():
            form.save()
            form = mariageForm()
            mssg = "acte ajouté, vous pouvez ajouté une autre"

            return render(request, "ajoutMariage.html", {"form": form, "message": mssg})
    else:
        form = mariageForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutMariage.html", {"form": form, "message ": mssg})

def ajout_deces(request):
    if request.method == 'POST':
        form = decesForm(request.POST)
        if form.is_valid():
            form.save()
            form = decesForm()
            mssg = "acte ajouté, vous pouvez ajouté une autre"

            return render(request, "ajoutDeces.html", {"form": form, "message": mssg})
    else:
        form = decesForm() #créer une instance de formulaire vierge
    mssg = "veuillez remplir tous les champs"
    return render(request, "ajoutDeces.html", {"form": form, "message ": mssg})

def login(request):
    if request.POST:
        username=request.POST['username']
        password=request.POST['password']
        form=loginForm(request.POST)
        if form.is_valid():
            check=User.objects.filter(username=username) and User.objects.filter(password=password).exists()
            if check:
                messages.success(request,'vous etes connecté ..')
                return redirect('/ajout_naissance')
            else:
                messages.success(request,'mot de passe ou nom utilisateur incorrect ! ')
                return redirect('/loginPage')
    else:
        form=loginForm()
    return  render(request,'login.html',{'form':form})


def searchN(request):
    acte_list = Naissance.objects.all()
    acte_filter = acteFilter(request.GET, queryset=acte_list)
    return render(request, 'searchN.html', {'filter': acte_filter})


def edit(request, id):
    acte = Naissance.objects.get(id=id)
    nom=acte.nom    
    marie=Mariage.objects.filter(nom_requerant1=nom)  
    lieumar=Mariage.objects.get(nom_requerant1=nom) 
    if marie :
        return render ( request , 'voir.html' , { 'acte' : acte ,'estmarie':'oui','lieumar':lieumar} )
    return render(request,'voir.html', {'acte':acte ,'estmarie':'non','marie':marie})

def editM(request, id):
    acte = Mariage.objects.get(id=id)
    
    return render(request,'voirM.html', {'acte':acte })

def editD(request, id):
    acte = Deces.objects.get(id=id)
    
    return render(request,'voirD.html', {'acte':acte })

def searchM(request):
    acte_list = Mariage.objects.all()
    acte_filter = MariageFilter(request.GET, queryset=acte_list)
    return render(request, 'searchM.html', {'filter': acte_filter})

def searchD(request):
    acte_list = Deces.objects.all()
    acte_filter = DecesFilter(request.GET, queryset=acte_list)
    return render(request, 'searchD.html', {'filter': acte_filter})