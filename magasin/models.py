from datetime import date
from django.db import models
# Create your models here.
class Categorie(models.Model):
    name=models.CharField(
    max_length=50,
    default='Alimentaire'
  )
    TYPE_CHOICES=[
      ('Al','Alimentaire'),
      ('Mb','Meuble'),
      ('Sn','Sanitaire'),
      ('Vs','Vaisselle'),
      ('Vt','Vêtement'),
      ('Jx','Jouets'),
      ('Lg','Linge de Maison'),
      ('Bj','Bijoux'),
      ('Dc','Décor')
    ]
    
    def __str__(self):
        return "Categorie : "+self.name
class Fournisseur(models.Model):
  nom=models.CharField(max_length=100)
  adresse=models.TextField()
  email=models.EmailField()
  telephone=models.CharField(max_length=8) 
  def __str__(self):
        return self.nom   

class Produit(models.Model):
  libelle = models.CharField(max_length=100)
  description = models.TextField(default='Non définie')
  prix=models.DecimalField(max_digits=10,decimal_places=3)
  TYPE_CHOICES=[
    ('em','emballé'),
    ('fr','Frais'),
    ('cs','Conserve')
  ]
  type=models.CharField(
    max_length=2,
    choices=TYPE_CHOICES,
    default='em'
  )
  img=models.ImageField(blank=True)
  categorie=models.ForeignKey(
    Categorie,
    on_delete=models.CASCADE,
    null=True

    )
  Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
  
  def __str__(self):
    return (self.libelle+' '+self.description+' '+str(self.prix))
class ProduitNC(Produit,models.Model):
  Duree_garantie=models.CharField(max_length=100)
  def __str__(self):
        return super().__str__()+" Garantie : "+self.Duree_garantie
class Commande(models.Model):
  dateCde=models.DateField(null=True,default=date.today)  
  totalCde=models.DecimalField(max_digits=10,decimal_places=3)
  produits=models.ManyToManyField("Produit")
  def __str__(self):
        return "Date Commande : "+ str(self.dateCde)
  
      
  
  
 