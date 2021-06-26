from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from accounts.forms import RegistrationForm,AccountUpdateForm


# Create your views here.
# This is login def
def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username , password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('landing')
                        
        else:
            messages.info(request,'Invalid credentials')
            return redirect('login')

       
    else:
        return render(request,'login.html')





# Create your views here####################################################
#This is register def
'''

class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = "register.html"
    success_url = reverse_lazy('login/')

'''

def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get("first_name")
            last_name = form.cleaned_data.get("last_name")
            email = form.cleaned_data.get("email")
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            account = authenticate(email = email, password = raw_password )
            return redirect('/')
        else:
             context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request,'register.html',context)

'''
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
    
        

        if password1 == password2 :
            if User.objects.filter(username= username).exists():
                messages.info(request,'Username Taken')
                return redirect ('register')
            elif User.objects.filter(email = email).exists():
                messages.info(request,'Email ID not available')
                return redirect ('register')
            else:
                user = User.objects.create_user(username = username, password = password1 , email = email, first_name = first_name , last_name = last_name)
                user.save()
                return redirect('login')
        
        else:
            messages.info(request,"password not matching")
            return redirect ('register')
        


    
    
    
    
    
    else:
        return render(request,'register.html')

'''

# Create your views here####################################################
#This is Logout def


def Logout(request):
    auth.logout(request)
    return redirect('/')

'''

class UserEditView(generic.CreateView):
    form_class = UserChangeForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('landing')

    def get_object(self):
        return self.request.user
    

'''
def account_view(request):
    context = {}

    if request.POST:
        form = AccountUpdateForm(request.POST, instance = request.user)
        if form.is_valid():
            form.save()
    else:
            form = AccountUpdateForm(
                initial = {
                    "first_name" : request.user.first_name,
                    "last_name" : request.user.last_name,
                     "email" : request.user.email,
                }
            )
    context['account_form'] = form 
    return render(request,'edit_cred.html',context)
