from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from .models import Product
from math import ceil

def index(request):
    # return HttpResponse("Index of Shops")

    products=Product.objects.all()
    print(products)
    n=len(products)
    nSlides = n//4 + ceil((n/4)-(n//4))

    params={'product':products, 'no_of_slides':nSlides, 'range':range(1,nSlides)}

    return render(request, 'shop/index.html', params)

def about(request):
    # return HttpResponse("About of Shops")
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse("contact of Shops")
def tracker(request):
    return HttpResponse("tracker of Shops")
def search(request):
    return HttpResponse("search of Shops")
def productView(request):
    return HttpResponse("prodView of Shops")
def checkout(request):
    return HttpResponse("checkout of Shops")
