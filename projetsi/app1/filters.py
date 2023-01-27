import django_filters
from django_filters import filters

from .models import *

class acteFilter(django_filters.FilterSet):
    date_naiss = filters.IsoDateTimeFilter ( field_name = 'date_naiss' )
    class Meta:
        model=Naissance
        fields=['nom','prenoms','date_naiss',]

class MariageFilter(django_filters.FilterSet):
    date_mariage = filters.IsoDateTimeFilter ( field_name = 'date_mariage' )
    class Meta:
        model=Mariage
        fields=['numero','nom_requerant1','prenom_requerant1','nom_requerant2','prenom_requerant2','date_mariage']

class DecesFilter(django_filters.FilterSet):
    date_naiss = filters.IsoDateTimeFilter ( field_name = 'date_naiss' )
    jour_deces = filters.IsoDateTimeFilter ( field_name = 'jour_deces' )
    class Meta:
        model=Deces
        fields=['nom','prenoms','date_naiss','jour_deces']
