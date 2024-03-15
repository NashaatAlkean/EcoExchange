from django.shortcuts import render
from items.models import Items
from users.models import User
from website.models import ReviewRating
from .forms import ReviewForm
from django.contrib import messages
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request,'website/home.html')


def items_listing(request):
    items=Items.objects.filter(is_available=True)
    context={'items':items}
    return render(request,'website/item_listing.html',context)

def item_details(request,pk):
    item=Items.objects.get(pk=pk)
    context={'item':item}
    return render(request,'website/item_details.html',context)


def reviews(request):
    # Your view logic for handling reviews
    return render(request, 'website/reviews.html')  # Assuming you have a template named reviews.html

def submit_review(request):
    url =request.META.get('HTTP_REFERER')
    if request.method =='POST':
       try:
           reviews = ReviewRating.objects.get(user__id =request.user.id)
           form = ReviewForm(request.POST, instance=reviews)
           form.save()
           messages.success(request,'Thank You Your review has been updated')
           return redirect(url)

       except ReviewRating.DoesNotExist:
           form = ReviewForm(request.POST)
           if form.is_valid():
               data = ReviewRating()
               data.subject =form.cleaned_data['subject']
               data.rating =form.cleaned_data['rating'] 
               data.review =form.cleaned_data['review']
               data.ip =request.META.get('REMOTE_ADDR')
               data.user__id =request.user__id
               data.save()
               messages.success(request,'Thank You Your review has been Submitted')
               return redirect(url)
