from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q
from django.core.paginator import Paginator,EmptyPage,InvalidPage

# Create your views here.

def home(request,c_slug=None):
    c_page=None
    prodt=None
    if c_slug!=None:
        c_page=get_object_or_404(categ,slug=c_slug)
        prodt=product.objects.filter(category=c_page,available=True)
    else:
        prodt=product.objects.all().filter(available=True)
    cat=categ.objects.all()
    paginator=Paginator(prodt,3)
    try:
        page=int(request.GET.get('page','1'))
    except:
        page=1
    try:
        pro=paginator.get_page(page)
    except(EmptyPage,InvalidPage):
        pro=Paginator.page(Paginator.num_pages)
    return render(request, 'hm.html.html', {'pr': prodt, 'ct': cat,'pg':pro})

def prodDetails(request,c_slug,product_slug):
    try:

        prod=product.objects.get(category__slug=c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'pr.html.html',{'pr':prod})

def searching(request):
    prod=None
    query=None
    if 'q'in request.GET:
        query=request.GET.get('q')
        prod=product.objects.all().filter(Q(name__contains=query)|Q(desc__contains=query))
    return render(request,'search.html',{'qr':query,'pr':prod})

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')