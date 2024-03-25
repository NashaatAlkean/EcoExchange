from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

# Create your views here.

from django.contrib import messages
from .models import Items,RequestsItems
from .form import DonateItemForm,UpdateItemForm

#create item ad
def create_item(request):
    if request.user.is_donor:
        if request.method=='POST':
            form=DonateItemForm(request.POST,request.FILES)
            # if len(request.FILES)!=0:
            #     form.image=request.FILES['image']
            if form.is_valid():
                var=form.save(commit=False)
                var.user =request.user
                var.save()
                messages.info(request,'Your ad has been send to admin approval!')
                return redirect('dashboard')
            else:
                messages.warning(request,'something wont wrong')
                return redirect('create-add')
        else:
            form=DonateItemForm()
            context={'form':form}
            return render(request,'items/create_ad.html',context)
        

    else:
        messages.warning(request,'You cant donate')
        return redirect('dashboard')


    
            
def update_item(request,pk):
    item=Items.objects.get(pk=pk)
    if request.method=='POST':
        form=UpdateItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            #var=form.save(commit=False)
            #var.user =request.user
            #var.save()
            messages.info(request,'Your updated ad has been send to admin approval!.')
            return redirect('dashboard')
        else:
            messages.warning(request,'something wont wrong')
    else:
        form=UpdateItemForm(instance=item)
        context={'form':form}
        return render(request,'items/update_ad.html',context)
    

def manage_items(request):
    items=Items.objects.filter(user=request.user)
    context={'items':items}
    return render(request,'items/manage_items.html',context)
    

def request_item(request,pk):
    if request.user.is_authenticated and request.user.is_seeker:
        item=Items.objects.get(pk=pk)
        if RequestsItems.objects.filter(user=request.user,item=pk).exists():
            messages.warning(request,'Permesion denied')
            return redirect('dashboard')
        else:
            RequestsItems.objects.create(
                item=item,
                user=request.user,
                status='Accepted'
            )
            messages.info(request,'You request this item!!')
            return redirect('dashboard')
    else:
        messages.info(request,'Login to continue')
        return redirect('login')
    

def all_requests(request,pk):
    item=Items.objects.get(pk=pk)
    seekerq=item.requestsitems_set.all()
    context={'item':item,'seekerq':seekerq}
    return render(request,'items/all_requests.html',context)


def requested_items(request):
    items=RequestsItems.objects.filter(user=request.user)
    context={'items':items}
    return render(request,'items/requested_items.html',context)

@login_required
def item_approval(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users

    items_to_approve = Items.objects.filter(is_approved=False)
    return render(request, 'website/items_approval.html', {'items': items_to_approve})


@login_required
def  approve_item(request, item_id):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users

    item = Items.objects.get(id=item_id)
    item.is_approved = True
    item.save()
    return redirect('item_approval')


@login_required
def decline_item(request, item_id):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect non-admin users

    item = Items.objects.get(id=item_id)
    item.delete()  # Delete the item from the database
    return redirect('item_approval')


