from django.db import models
from datetime import date
from django.utils import timezone

class User(models.Model):
    name = models.CharField(max_length=50, default='')
    password = models.CharField(max_length=50, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=20, default='')
    address = models.CharField(max_length=20, default='', null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['email']

    def __str__(self):
        return f'name={self.name}, email={self.email}, phone={self.phone}'
    #def create_user()
    #def create super_user()

class Vendeur(User):
    #propriete = models.ForeignKey(Propriete, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        
        db_table = 'vendeur'
        managed = True


    def __str__(self):
        return f'name={self.name}, email={self.email}, phone={self.phone}, site_url={self.site_url}'


class Offre(models.Model):
    prop_id = models.IntegerField(null=True, blank=True)
    type_proptiete=models.CharField(max_length=20,null=True, blank=True)
    surface = models.CharField(max_length=50, default='')
    nbr_chambre = models.PositiveIntegerField(default=0)
    nbr_sallebain = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='static/image/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
    type=models.CharField(max_length=20, default='')
    address = models.CharField(max_length=20, default='', null=True, blank=True)
    existe = models.BooleanField(default=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modif = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Prix en dinar")
    class Meta:
     db_table = 'Offre'

    #vendeur = models.ManyToManyField(Vendeur, related_name='offres', blank=True)

class Besoin(models.Model):
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    budget_max = models.PositiveBigIntegerField()
    type_propiete = models.CharField(max_length=20)
    surface_min = models.CharField(max_length=50)
    localisation = models.CharField(max_length=50)
    date_creation = models.DateTimeField(auto_now_add=True) 

    class Meta:
        db_table = 'besoin'

'''class Achat(models.Model):
    offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    date_achat = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'blog_achat'
    #il y'a une possibilite que tu veux faire l'achat ou faire une colocation'''

'''class Client(User):
    Offre = models.ForeignKey(Offre, on_delete=models.CASCADE)
    class Meta:
        db_table = 'client'
   
    def __str__(self):
        return f'name={self.name}, email={self.email}, phone={self.phone}, site_url={self.site_url}'''


