from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from items.models import Items
from .models import User,Profile
from .form import RegisterUserForm,ProfileForm
from django.contrib.auth.models import User as AuthUser
from django.contrib.auth.decorators import login_required, user_passes_test

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
            if user.is_superuser:
                return redirect('admin-homepage')  # Redirect to the view to select a user to impersonate

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



# Define a decorator to check if the user is a superuser
def is_superuser(user):
    return user.is_superuser


# @login_required
# @user_passes_test(is_superuser)
# def select_user_to_impersonate(request):
#     users = AuthUser.objects.exclude(is_superuser=True)
#     return render(request, 'dashboard\admindashboard.html', {'users': users})


    

# def approve_item(request, item_id):
#     item = Items.objects.get(id=item_id)
#     item.is_approved = True  
#     item.save()
#     return render('items_approval.html')

def user_list(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users
    users = User.objects.filter(is_superuser=False)
    return render(request, 'dashboard\\adminUsersList.html', {'users': users})

def delete_users(request):
    if not request.user.is_superuser:
        return redirect('home')
    if request.method == 'POST':
        user_ids = request.POST.getlist('user_ids')
        if user_ids:
            User.objects.filter(id__in=user_ids).delete()
    return redirect('user_list')


def profile(request,pk):
    if request.user.is_authenticated:
        profile=Profile.objects.get(user_id=pk)

        return render(request,"users/profile.html",{"profile":profile})
    else:
        messages.success(request,("You have to log in"))
        return redirect('dashboard')
    


def update_user(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        form=RegisterUserForm(request.POST or None, instance=current_user)
        if form.is_valid():
            form.save()
            login(request,current_user)
            messages.success(request,("Your information has been updated"))
            return redirect('dashboard')
        return render(request,"users/update_user.html",{'form':form})

    else:
        messages.success(request,("You have to log in"))
        return redirect('dashboard')
    

def update_profile(request):
    if request.user.is_authenticated:
        current_user=User.objects.get(id=request.user.id)
        profile_user=Profile.objects.get(user__id=request.user.id)
        profile_form=ProfileForm(request.POST or None,request.FILES or None, instance=profile_user)
        if profile_form.is_valid():
            profile_form.save()
            login(request,current_user)
            messages.success(request,("Your information has been updated"))
            return redirect('dashboard')
        return render(request,"users/update_profile.html",{'profile_form':profile_form})

    else:
        messages.success(request,("You have to log in"))
        return redirect('dashboard')
    


    