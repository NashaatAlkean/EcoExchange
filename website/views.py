from django.shortcuts import redirect, render
from items.models import Items,RequestsItems
from django.contrib.auth.decorators import login_required
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


def admin_homepage(request):
    return render(request,'dashboard/admindashboard.html')


# @login_required   
# def item_approval(request):
#     if not request.user.is_superuser:
#         return redirect('home')
#     items = Items.objects.filter(is_approved = False)
#     print(items)
#     return render(request, 'website/items_approval.html', {'items': items})

# @login_required
# def approve_item(request, item_id):
#     if not request.user.is_superuser:
#         return redirect('home')

#     item = Items.objects.get(id=item_id)
#     item.is_approved = True  #  True indicates approval
#     item.save()
#     return redirect('item_approval')