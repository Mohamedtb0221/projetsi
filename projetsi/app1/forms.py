from django import forms
from .models import *

class officierForm (forms.ModelForm):

    class Meta:
        model = Officier
        fields = [ 'matricule', 'nom', 'prenom','datePriseService' ]
        widgets = {
            'datePriseService': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class naissanceForm(forms.ModelForm):
    class Meta:
        model=Naissance
        fields = "__all__"
        widgets={
            'officier':forms.NumberInput(attrs = {'class':'form-control'}),
            'numero_registre':forms.Select(attrs = {'class':'form-control'}),
            'annee' : forms.NumberInput ( attrs = { 'class' : 'form-control' }),
            'nom' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'prenoms' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'sexe' : forms.Select ( attrs = { 'class' : 'form-control' },choices = (('M','Masculin'),('F','Feminin'))),
            'hopital':forms.Select ( attrs = { 'class' : 'form-control' },),
            'date_naiss':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'date de naissance', 'type':'date'}),
            'heure_naiss':forms.TimeInput(format = ('%h/%m/%s'),attrs = {'class':'form-control','placeholder':'heure de naissance','type':'time'}),
            'pays':forms.TextInput(attrs = {'class':'form-control'}),
            'pere':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'date_naiss_pere':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'date de naissance de pere', 'type':'date'}),
            'lieu_naiss_pere':forms.TextInput(attrs = {'class':'form-control'}),
            'profession_pere':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'mere':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'date_naiss_mere' : forms.DateInput ( format = ('%m/%d/%Y') , attrs = { 'class':'form-control' ,'placeholder' : 'date de naissance de mere' ,'type' : 'date' } ) ,
            'lieu_naiss_mere' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'profession_mere':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'grand_pere_paternel':forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'grand_mere_paternel' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'grand_pere_maternel' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'grand_mere_maternel' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,

        }

class mariageForm(forms.ModelForm):
    class Meta:
        model=Mariage
        fields = ['officier','numero_registre','nom_requerant1','prenom_requerant1','profession_req1','domicile_req1','date_req1','lieu_naiss_req1', 'temoin_req1','nom_requerant2','prenom_requerant2','profession_req2','domicile_req2','date_req2','lieu_naiss_req2', 'temoin_req2','filiation','date_mariage','lieu_mariage']
        widgets={
            'officier':forms.NumberInput(attrs = {'class':'form-control'}),
            'numero_registre':forms.NumberInput(attrs = {'class':'form-control'}),
            'numero':forms.NumberInput(attrs = {'class':'form-control'}),
            'nom_requerant1':forms.TextInput(attrs = {'class':'form-control'}),
            'prenom_requerant1' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'profession_req1':forms.TextInput(attrs = {'class':'form-control'}),
            'domicile_req1':forms.TextInput(attrs = {'class':'form-control'}),
            'date_req1':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'date de naissance', 'type':'date'}),
            'lieu_naiss_req1':forms.TextInput(attrs = {'class':'form-control'}),
            'temoin_req1':forms.TextInput(attrs = {'class':'form-control'}),
            'nom_requerant2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'prenom_requerant2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'profession_req2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'domicile_req2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'date_req2':forms.DateInput(format=('%m/%d/%Y'),attrs = { 'class' : 'form-control' , 'placeholder' : 'date de naissance' ,'type' : 'date' } ) ,
            'lieu_naiss_req2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'temoin_req2' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'filiation':forms.TextInput(attrs = {'class':'form-control'}),
            'date_mariage':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'date de mariage', 'type':'date'}),
            'lieu_mariage' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,

        }

class decesForm(forms.ModelForm):
    class Meta:
        model=Deces
        fields = "__all__"
        widgets={
            'officier':forms.NumberInput(attrs = {'class':'form-control'}),
            'numero_registre':forms.NumberInput(attrs = {'class':'form-control'}),
            'nom' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'prenoms' : forms.TextInput ( attrs = { 'class' : 'form-control' } ) ,
            'sexe' : forms.Select ( attrs = { 'class' : 'form-control' },choices = (('M','Masculin'),('F','Feminin'))),
            'date_naiss':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'date de naissance', 'type':'date'}),
            'lieu_naiss':forms.TextInput(attrs = {'class':'form-control'}),
            'mariée':forms.Select ( attrs = { 'class' : 'form-control' },choices = (('oui','OUI'),('non','NON'))),
            'jour_deces':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'date de naissance', 'type':'date'}),
            'heure_deces':forms.TimeInput(format = ('%h/%m/%s'),attrs = {'class':'form-control','placeholder':'heure de naissance','type':'time'}),
            'lieu_deces':forms.TextInput(attrs = {'class':'form-control'})
        }

class loginForm(forms.ModelForm):


    class Meta :
        model = User
        fields = ('username','password')
        widgets={
            'username':forms.TextInput(attrs = {'class':'form-control form-control-lg','placeholder': "Nom d'utilisateur"}),
            'password':forms.PasswordInput(attrs = {'class':'form-control form-control-lg','placeholder': "Mot de passe"}),
        }


