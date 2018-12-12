from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.decorators import login_required
from .models import Address, STATES_CHOICES


# Create your views here.
def login(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'my_app/login.html')

        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username)
        # print(password)

        user = authenticate(username=username, password=password)
        # print(vars())

        if user:
            django_login(request, user)
            # next_param = request.get('next')
            # return HttpResponse('usuário Válido')
            # return HttpResponseRedirect('/home/')
            return redirect('/home/')
        message = 'Credenciais inválidas'
        return render(request, 'my_app/login', {'message': message})


@login_required(login_url='/login')
def logout(request):
    django_logout(request)
    return redirect('/logout/')


@login_required(login_url='/login')
def home(request):
    return render(request, 'my_app/home.html')


@login_required(login_url='/login')
def address_list(request):
    addresses = Address.objects.all()
    return render(request, 'my_app/address/list.html', {'addresses': addresses})


@login_required(login_url='/login')
def address_create(request):
    if request.method == 'GET':
        states = STATES_CHOICES
        return render(request, 'my_app/address/create.html', {'states': states})

    Address.objects.create(
        address=request.POST.get('address'),
        address_complement=request.POST.get('address'),
        city=request.POST.get('address_complement'),
        state=request.POST.get('state'),
        country=request.POST.get('address_complement'),
        user=request.user
    )

    return redirect('/addresses/')


@login_required(login_url='/login')
def address_update(request, id):
    address = Address.objects.get(id=id)
    if request.method == 'GET':
        states = STATES_CHOICES
        return render(request, 'my_app/address/create.html', {'states': states, 'address': address})

    address.address = request.POST.get('address')
    address.address_complement = request.POST.get('address')
    address.city = request.POST.get('address_complement')
    address.state = request.POST.get('state')
    address.country = request.POST.get('address_complement')
    # NÃO ATUALIZA O USER
    # address.user = request.user

    address.save()

    return redirect('/addresses/')
