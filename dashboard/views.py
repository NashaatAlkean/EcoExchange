from django.shortcuts import render,redirect

# Create your views here.

# def proxy(request):
#     if request.user.is_seeker:
#         return redirect('seeker-dashboard')
#     elif request.user.is_donor:
#         return redirect('donor-dashboard')
#     else:
#         return redirect('login')

# def seeker_dashboard(request):
#     return render(request,'dashboard/seeker_dashboard.html')

# def donor_dashboard(request):
#     return render(request,'dashboard/donor_dashboard.html')

def dashboard(request):
    return render(request,'dashboard/dashboard.html')




    
