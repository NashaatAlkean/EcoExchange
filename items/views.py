from django.shortcuts import render,redirect

# Create your views here.

from django.contrib import messages
from .models import Items
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
                messages.info(request,'New item has been published..')
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
            messages.info(request,'Your items info has updated.')
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
    




