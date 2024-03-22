from django.shortcuts import redirect, render
from items.models import Items,RequestsItems
from .filter import Itemfilter

from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    filter=Itemfilter(request.GET,queryset=Items.objects.filter(is_available=True).order_by('-updated_at'))
    context={'filter':filter}
    return render(request,'website/home.html',context)


def items_listing(request):
    items=Items.objects.filter(is_available=True).order_by('-updated_at')
    context={'items':items}
    return render(request,'website/item_listing.html',context)

def item_details(request,pk):
    if RequestsItems.objects.filter(user=request.user.id,item=pk).exists():
        has_req=True
    else:
        has_req=False
    item=Items.objects.get(pk=pk)
    context={'item':item,'has_req':has_req}
    return render(request,'website/item_details.html',context)


def reviews(request):
    return render(request, 'website/reviews.html') 
    # Your view logic for handling reviews
    return render(request, 'website/reviews.html')  # Assuming you have a template named reviews.html


def admin_homepage(request):
    if not request.user.is_superuser:
        return redirect('home')
    return render(request,'dashboard/adminHomePage.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Import login_required decorator
from .forms import ReviewForm
from .models import ReviewRating


@login_required
def reviews(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user  # Assign the current user to the review
            new_review.ip = request.META['REMOTE_ADDR']
            new_review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews_list = ReviewRating.objects.all() # Query reviews and order by creation time
    return render(request, 'website/reviews.html', {'form': form, 'reviews_list': reviews_list, 'user': request.user})