from django.shortcuts import render
from django.http import HttpResponse
from .models import Room,Topic,tryform,User
from .forms import RoomForm,tryform
from django.db.models import Q
from django.contrib.messages import constants as messages#import redirect
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def loginPage(request):
    page = 'login'
    print('login page ')
    print(request.user.is_authenticated)
    if(request.user.is_authenticated):
        print('user logged in')
        return redirect('home')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,'User does not exist')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print('user logged in')
            return redirect('home')
        else:
            messages.error(request,'User OR PARRWORD not exist')
            context = {'page':page}
        return render(request,'base/login_register.html',context)
    context = {'page':page}
    return render(request,'base/login_register.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')
    
    
def registerPage(request):
    form = UserCreationForm()
    if(request.method=='POST'):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'An error occured during registration')
            
    context = {'form':form}
    return render(request,'base/login_register.html',context)
def home(request):
   
    topics = Topic.objects.all()  # Fetch all topics  
    rooms = Room.objects.all()
    q = request.POST.get('q')
    if request.POST.get('q') != None:  
        rooms = rooms.filter(
            Q(topic__name__icontains=q) 
            | Q(name__icontains=q)
            | Q(description__icontains=q)
        )
    total_rooms = rooms.count()
    context = {'topics': topics, 'rooms': rooms,'total_rooms':total_rooms}
    return render(request, 'base/home.html',context=context)
def room(request,pk):
    room = Room.objects.get(id=pk) 
    context = {"rooms":room}
    return render(request,'base/room.html',context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)


@login_required(login_url='login')
def updateRoom(request,pk):
    room  = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.user != room.host:
        return HttpResponse('You are not allowed here')
    if request.method == 'POST':
        form = RoomForm(request.POST,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    return render(request,'base/room_form.html',context)
    

@login_required(login_url='login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if(request.method == 'POST'):
        room.delete()
        return redirect('home')
    context = {'obj':room}
    return render(request,'base/delete.html',context)


    
def tryform(request):
    form = tryform()
    if request.method == 'POST':
        form = tryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form':form}
        
    return render(request,'base/tryform.html',context)
        
    