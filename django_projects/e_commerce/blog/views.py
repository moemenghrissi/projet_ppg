from django.shortcuts import render,redirect
from .models import Offre,Besoin
from .form_ajout_bien import Offresform


def view_offres(request):
    offres = Offre.objects.all()
    return render(request, 'home.html', {'offres': offres})


def formulaire(request):
    return render(request, "formulaire.html")

def location(request):
    list_offers = Offre.objects.all()
    context = {"list_offers": list_offers}
    return render(request, "location.html", context)

def vente(request):
    list_offers = Offre.objects.all()
    context = {"list_offers": list_offers}
    return render(request, "vente.html", context)

def resultat_recherche(request):
    return render(request, "resultat.html")

#mate5dmch ye jhon 
def recherche(request):
    budget_max = request.GET.get('budget_max')
    if budget_max is not None:
        besoins = Besoin.objects.filter(budget_max__lte=budget_max)
        if 'surface_min' in request.GET:
            surface_min = request.GET.get('surface_min')
            besoins = besoins.filter(surface_min__lte=surface_min)
        if 'adresse' in request.GET:
            adresse = request.GET.get('adresse')
            besoins = besoins.filter(localisation__icontains=adresse)
        offres_correspondantes = []
        for besoin in besoins:
            offres = Offre.objects.filter(surface__gte=besoin.surface_min, address__icontains=besoin.localisation, type_proptiete=besoin.type_propiete, existe=True, price__lte=besoin.budget_max)
            for offre in offres:
                offres_correspondantes.append(offre)
        context = {'offres': offres_correspondantes}
        return render(request, 'resultat.html', context)
   


def ajout_bien(request):
    if request.method == "POST":
        form = Offresform (request.POST)
        if form.is_valid():
            form.save()
            return redirect('/ajout_bien')
    else:
        form = Offresform()
    return render(request, 'form_ajout_bien.html', {'form': form})

# Create your views here.
