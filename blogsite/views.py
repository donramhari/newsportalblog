from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from . forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def main(request):
    return render(request, 'main.html',context = {'posts': Post.objects.all().order_by("-id")[:3]})

@login_required(login_url='login')
def postdetail(request, id):
    return render(request, 'postdetail.html',context = {'posts': Post.objects.get(id=id)})

@login_required(login_url='login')
def allposts(request):
    posts = Post.objects.all().order_by("-id")
    return render(request, 'allposts.html', {'posts': posts})


def registerPage(request):
    
    if request.user.is_authenticated:
        return redirect('main')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account created for ' + user )
                return redirect('login')

        context = { 'form':form }
        return render (request, 'register.html', context )

def loginPage(request):

    if request.user.is_authenticated:
        return redirect ('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                    login(request,user)
                    return redirect('main')
            else:
                messages.info(request, 'Username or password incorrect ')
                

        context = {}
        return render (request, 'login.html', context )


def logoutUser(request):
    logout(request)
    return redirect ('login')