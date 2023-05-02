from django.urls import path
from . import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.view_offres, name='offre'),
    path('formulaire', views.formulaire, name='formulaire'),
    path('location', views.location, name='location'),
    path('vente', views.vente, name='vente'),
    path('recherche/', views.recherche, name='recherche'),
    path('ajout_bien', views.ajout_bien, name='ajout_bien'),
    path('recherche_resultat/', views.resultat_recherche, name='recherche_resultat'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)