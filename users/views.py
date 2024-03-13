from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import User
from .form import RegisterUserForm

#import our user model and our RegistercUsercForm
# Create your views here.


#register seeker only
def register_seeker(request):
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_seeker=True
            var.username=var.email
            #the username became automaticly the email
            var.save()
            #Activatee.objects.create(user=var)
            messages.info(request,'Your acoount has been created...')
            return redirect('login')
        else:
            messages.warning(request,'something went wrong')
            return redirect('register-seeker')
    else:
        form=RegisterUserForm()
        contex={'form':form}
        return render( request,'users/register_seeker.html',contex)
    

#register donor only
    
def register_donor(request):
    if request.method=='POST':
        form=RegisterUserForm(request.POST)
        if form.is_valid():
            var=form.save(commit=False)
            var.is_donor=True
            var.username=var.email
            var.save() 
            #Donoractive.objects.create(user=var)
            messages.info(request,'Your acoount has been created,please login')
            return redirect('login')
        else:
            messages.warning(request,'something went wrong')
            return redirect('register-donor')
    else:
        form=RegisterUserForm()
        contex={'form':form}
        return render( request,'users/register_donor.html',contex)


#user login
def login_user(request):
    if request.method=='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        user=authenticate(request,username=email,password=password)
        if user is not None and user.is_active:
            login(request,user)
            # if request.user.is_seeker:
            #     return redirect('seeker-dashboard')
            # elif request.user.is_seeker:
            #     return redirect('donor-dashboard')
            # else:
            #     return redirect('login')
            return redirect('home')
        else:
            messages.warning(request,'somthing went wrong')
            return redirect('login')
    else:
        return render(request,'users/login.html')
    


#user logout
def logout_user(request):
    logout(request)
    messages.info(request,'your session has ended')
    return redirect('home')


            
            







    
 
