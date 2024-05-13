from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import  HttpResponseRedirect
from django.template import loader
from .forms import ProduitForm
from .models import Produit,Commande,Categorie
from magasin.serializers import CategorySerializer,ProduitSerializer
from rest_framework import viewsets
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect ,render
from django.contrib.auth.decorators import login_required


class ProductViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class = ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('categorie_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset

class CategoryAPIView(APIView):
 def get(self, *args, **kwargs):
    categories = Categorie.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)
 
class ProduitAPIView(APIView):
 def get(self, *args, **kwargs):
    categories = Produit.objects.all()
    serializer = ProduitSerializer(categories, many=True)
    return Response(serializer.data)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Hello {username}, Your account has been created successfully!')
            return redirect('index') 
        else:
            # Render the registration form again with errors
            return render(request, 'registration/register.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'registration/register.html', {'form': form})


@login_required
def index(request):	
    template = loader.get_template('magasin/mesProduits.html')
    products = Produit.objects.all()
    context = {'products': products}
    return render(request, 'magasin/mesProduits.html', context)
@login_required
def modifier(request):
  if request.method == "POST" : 
    form = ProduitForm(request.POST,request.FILES) 
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/magasin') 
  else : 
    form = ProduitForm()
  return render(request,'magasin/majProduits.html',{'form':form}) 
@login_required
def vitrine(request):
  list=Produit.objects.all()
  return render(request,'magasin/vitrine.html',{'list':list})
  