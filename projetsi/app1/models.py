import datetime

from django.db import models

# Create your models here.
Sexe=(
    ('HOMME','homme'),
    ('FEMME','femme')
)


class User(models.Model):
    username = models.CharField(max_length = 100)
    password = models.CharField(max_length = 100)




def matricul():
    no = Officier.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class Officier(models.Model):
    matricule = models.BigIntegerField(unique = True,default=matricul)
    nom = models.CharField(max_length = 50)
    prenom = models.CharField(max_length = 50)
    datePriseService = models.DateField()

class Centre(models.Model):
    libelle_centre = models.CharField(max_length=500, verbose_name="Centre de Santé")
    situation = models.CharField(max_length=500, verbose_name="Situation Geographique du Centre")

    def __str__ ( self ) :
        return str ( self.libelle_centre )

class RegistreNaissance(models.Model):
    numero_registre = models.CharField ( max_length = 150 , verbose_name = 'Numero du Registre',primary_key=True )
    annee = models.IntegerField ( verbose_name = 'Annee' , default = datetime.datetime.now ( ).year )

    def __str__ ( self ) :
        return str ( self.numero_registre )

class RegistreMariage(models.Model):
    numero_registre = models.CharField ( max_length = 150 , verbose_name = 'Numero du Registre',primary_key=True )
    annee = models.IntegerField ( verbose_name = 'Annee' , default = datetime.datetime.now ( ).year )

    def __str__ ( self ) :
        return str ( self.numero_registre )

class RegistreDeces(models.Model):
    numero_registre = models.CharField ( max_length = 150 , verbose_name = 'Numero du Registre',primary_key=True )
    annee = models.IntegerField ( verbose_name = 'Annee' , default = datetime.datetime.now ( ).year )

    def __str__ ( self ) :
        return str ( self.numero_registre )


class Naissance(models.Model):
    officier=models.ForeignKey(Officier,on_delete=models.CASCADE,default=0)
    numero_registre = models.ForeignKey(RegistreNaissance,on_delete=models.CASCADE ,default = 0)
    # informations recipiendaire
    sexe = models.CharField(max_length=150, verbose_name='Precise le sexe', choices=Sexe,default = 'Masculin')
    nom = models.CharField(max_length=250, verbose_name='Nom')
    prenoms = models.CharField(max_length=250, verbose_name='Prenoms')
    date_naiss = models.DateField(verbose_name='Date de Naissance',null = True)
    heure_naiss = models.TimeField(verbose_name='Heure de Naissance')
    hopital = models.ForeignKey(Centre,on_delete=models.CASCADE)
    pays=models.CharField(max_length = 50,verbose_name = 'pays de naissance',default = 'Algérie')
    # parents
    pere = models.CharField(max_length=250, verbose_name='Nom et Prénoms du Pere', blank=True)
    profession_pere = models.CharField(max_length=250, verbose_name='Profession du Pere', blank=True)
    date_naiss_pere = models.DateField ( verbose_name = 'Date de Naissance',null = True)
    lieu_naiss_pere = models.CharField ( max_length = 250 , verbose_name = 'Lieu de Naissance',default = '' )
    mere = models.CharField(max_length=250, verbose_name='Nom et Prénoms de la Mere')
    profession_mere = models.CharField(max_length=250, verbose_name='Profession de la Mere')
    date_naiss_mere = models.DateField ( verbose_name = 'Date de Naissance',null = True)
    lieu_naiss_mere = models.CharField ( max_length = 250 , verbose_name = 'Lieu de Naissance',default = '' )
    # grand-parents
    grand_pere_paternel=models.CharField(max_length=250, verbose_name='Nom et Prénoms du grand Pere', blank=True,default = '')
    grand_mere_paternel = models.CharField ( max_length = 250 , verbose_name = 'Nom et Prénoms du grand mere' ,blank = True ,default = '')
    grand_pere_maternel = models.CharField ( max_length = 250 , verbose_name = 'Nom et Prénoms du grand Pere' ,blank = True ,default = '')
    grand_mere_maternel = models.CharField ( max_length = 250 , verbose_name = 'Nom et Prénoms du grand mere' ,blank = True ,default = '')


def num_mariage():
    no = Mariage.objects.count()
    if no == None:
        return 1
    else:
        return no + 1

class Mariage(models.Model):
    officier=models.ForeignKey(Officier,on_delete=models.CASCADE,default=0)
    numero_registre = models.ForeignKey ( RegistreMariage , on_delete = models.CASCADE,default = 0 )
    numero = models.CharField(max_length=5, unique=True, default=num_mariage)
    nom_requerant1 = models.CharField ( max_length = 500 , verbose_name = "Nom du Marie" ,default = ' ')
    prenom_requerant1 = models.CharField ( max_length = 500 , verbose_name = "Prenom du Marie",default = ' ' )
    profession_req1 = models.CharField ( max_length = 500 , verbose_name = "Profession du Marie" )
    domicile_req1 = models.CharField ( max_length = 500 , verbose_name = "Lieu de Domicile du Marie" )
    date_req1 = models.DateField ( verbose_name = "Date de Naissance du Marie" )
    lieu_naiss_req1 = models.CharField ( max_length = 500 , verbose_name = "Lieu de Naissance du Marie" )
    temoin_req1 = models.CharField ( max_length = 250 , verbose_name = 'Nom et Prénoms du Témoin du Marie' )
    nom_requerant2 = models.CharField ( max_length = 500 , verbose_name = "Nom du Mariee",default = ' ' )
    prenom_requerant2 = models.CharField ( max_length = 500 , verbose_name = "Prenom du Mariee",default = ' ' )
    profession_req2 = models.CharField ( max_length = 500 , verbose_name = "Profession du Mariee" )
    domicile_req2 = models.CharField ( max_length = 500 , verbose_name = "Lieu de Domicile du Mariee" )
    date_req2 = models.DateField ( verbose_name = "Date de Naissance du Mariee" )
    lieu_naiss_req2 = models.CharField ( max_length = 500 , verbose_name = "Lieu de Naissance du Mariee" )
    temoin_req2 = models.CharField ( max_length = 250 , verbose_name = 'Nom et Prénoms du Témoin du Mariee' )
    filiation = models.CharField ( max_length = 500 , verbose_name = 'la filiation',default = ' ' )
    date_mariage = models.DateField ( verbose_name = "Date du Mariage" )
    lieu_mariage = models.CharField ( max_length = 500 , verbose_name = "Lieu du Mariage" )


class Deces(models.Model):
    officier=models.ForeignKey(Officier,on_delete=models.CASCADE,default=0)
    numero_registre = models.ForeignKey ( RegistreDeces , on_delete = models.CASCADE,default = 0 )
    nom = models.CharField ( max_length = 250 , verbose_name = 'Nom' )
    prenoms = models.CharField ( max_length = 250 , verbose_name = 'Prenoms' )
    sexe = models.CharField ( max_length = 150 , verbose_name = 'Precise le sexe' , choices = Sexe ,default = 'Masculin' )
    date_naiss = models.DateField ( verbose_name = 'Date de Naissance' )
    lieu_naiss = models.CharField ( max_length = 250 , verbose_name = 'Lieu de Naissance' )
    mariée=models.CharField(max_length = 10,choices = (('oui','OUI'),('non','NON')),default = 'NON')
    jour_deces=models.DateField ( verbose_name = 'Date de deces' )
    heure_deces=models.TimeField ( verbose_name = 'Heure de deces' )
    lieu_deces=models.CharField ( max_length = 250 , verbose_name = 'Lieu de deces' )
