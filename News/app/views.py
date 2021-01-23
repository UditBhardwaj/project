from django.shortcuts import render,redirect,HttpResponse
from .models import Article,Contact
from django.views.generic import ListView,DetailView,CreateView,DeleteView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegisterForm
from django.views.generic.edit import CreateView
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
  
class ArticleCreate(CreateView):
    model = Article
    template_name = 'add.html'
    fields = '__all__'

class ListArticles(ListView):
    model = Article
    template_name = 'list.html'

class DetailArticle(DetailView):
    model = Article
    template_name = 'detail.html'

class DeleteArticle(DeleteView):
    model = Article
    template_name = 'confirm_delete.html'
    success_url ="/"

class UpdateArticle(UpdateView): 
    model = Article 
    fields = [ 
        "title", 
        "description"
    ] 
    template_name = 'update.html'
    success_url ="/"


def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        contact=Contact(name=name, email=email, phone=phone, content=content)
        contact.save()
        messages.success(request, "Your message has been successfully sent")
    return render(request, "contact.html")

def handeLogin(request):
    if request.method=="POST":
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']

        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully Logged In")
            return redirect('/')
        else:
            messages.error(request, "Invalid credentials! Please try again")
            return redirect('/')

    return HttpResponse("404- Not found")


def handelLogout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/')

def handleSignUp(request):
    if request.method == "POST":
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        myuser = User.objects.create_user(username, email, pass1)
        myuser.save()
        messages.success(request, " Your account has been successfully created")
        return redirect('/')
    
    else:
        return HttpResponse("404 - Not found")

def about(request): 
    return render(request, "about.html")
    
def home(request):
    return render(request, "home.html")