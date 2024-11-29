from django.shortcuts import render

from . models import Product

# Create your views here.
def index(request):

    pro=Product.objects.all()


    return render(request,'home.html',{'pro':pro})


    
