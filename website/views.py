from django.shortcuts import render
from items.models import Items,RequestsItems
# Create your views here.

def home(request):
    return render(request,'website/home.html')


def items_listing(request):
    items=Items.objects.filter(is_available=True)
    context={'items':items}
    return render(request,'website/item_listing.html',context)

def item_details(request,pk):
    if RequestsItems.objects.filter(user=request.user,item=pk).exists():
        has_req=True
    else:
        has_req=False
    item=Items.objects.get(pk=pk)
    context={'item':item,'has_req':has_req}
    return render(request,'website/item_details.html',context)


def reviews(request):
    # Your view logic for handling reviews
    return render(request, 'website/reviews.html')  # Assuming you have a template named reviews.html