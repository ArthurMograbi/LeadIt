from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Vector,Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
#from django.contrib.auth.decorators import login_required
import random


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def regi(request, vector_id):
    vec=get_object_or_404(Vector,code=vector_id)
    try:
        #print("AQUI",request.POST)
        new_client = Client()
        new_client.papi=vec
        new_client.name=request.POST['nome']
        new_client.age=request.POST['idade']
        new_client.job=request.POST['trabalho']
        if 'filhos' in request.POST:
            new_client.kids=int(request.POST['filhos'])
        new_client.join_date=timezone.now()
        new_client.code = str(new_client.add_value(70,new=True))
        new_client.save()
        
    except (KeyError, Vector.DoesNotExist):
        return render(request, 'register/regi.html',{'vec': vec})#, {'vec': vec,'err':'Error'})
    return HttpResponseRedirect(reverse('regi2', args=[vec.code ,new_client.code]))#render(request, 'register/regi.html', {'vec': vec})

def regi2(request, vector_id, client_id):
    vec=get_object_or_404(Vector,code=vector_id)
    cli=get_object_or_404(Client,papi=vec,code=client_id)
    try:
        cli.cel=request.POST['cel']
        cli.email=request.POST['email']
        cli.cpf=request.POST['cpf']
        cli.save()
        cli.add_value(15)
    except (KeyError, Vector.DoesNotExist):
        return render(request, 'register/regi2.html',{'vec': vec,'cli':cli})#, {'vec': vec,'err':'Error'})
    return HttpResponseRedirect(reverse('subm', args=[vec.code]))
    
def subm(request, vector_id):
    vec=get_object_or_404(Vector,code=vector_id)
    #vec=get_object_or_404(Vector,code=vector_id)
    return render(request, 'register/subm.html', {'vec': vec})


def welcome(request):
    try:
        n = request.POST['usern']
        e = request.POST['email']
        p = request.POST['pw']
        user = User.objects.create_user(n,e,p)
        new_vector=Vector(name=n,
                          username=n,
                          password=p,
                          code=str(random.randint(1000,9999)),
                          join_date=timezone.now()
                          )
        new_vector.save()
    except (KeyError):
        return render(request, 'register/welcome.html')#, {'vec': vec,'err':'Error'})
    return render(request, 'register/welcome2.html', {'vec': new_vector})#HttpResponseRedirect(reverse('subm', args=[vec.code]))


def vec_page(request,vector_id):
    vec=get_object_or_404(Vector,code=vector_id)
    cli_list=[]
    for i in range(vec.cnum):
        cli_list.append(get_object_or_404(Client,papi=vec,code=str(i+1)))
    return render(request, 'register/vec_page.html', {'vec':vec,'clist':cli_list})
    
def leaderboard(request):
    vecs=Vector.objects.order_by('balanca')
    return render(request, 'register/leaderboard.html', {'vecs':vecs})
