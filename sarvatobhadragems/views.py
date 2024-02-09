from django.shortcuts import redirect, render
from gems.models import *

def BASE(request):
    return render(request,'base.html') 

def Home(request):
    reviews = Review.objects.all()
    context = {'reviews':reviews}
    return render(request,'main/home.html',context) 

def About(request):
    return render(request,'main/about.html') 

def products(request):
    return render(request,'products/products.html') 

def beads_jewellery(request):
    return render(request,'products/beads-jewellery.html') 

def cabochon(request):
    return render(request,'products/cabochon.html') 

def diamond_products(request):
    return render(request,'products/diamond-products.html') 

def emerald_gemstone(request):
    return render(request,'products/emerald-gemstone.html') 

def faceted_stone(request):
    return render(request,'products/faceted-stone.html') 

def handicraft_products(request):
    return render(request,'products/handicraft-products.html') 

def jewellery(request):
    return render(request,'products/jewellery.html') 

def natural_rough_gemstone(request):
    return render(request,'products/natural-rough-gemstone.html') 

def rashi_ratan(request):
    return render(request,'products/rashi-ratan.html') 

