from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Items
from .form import DonateItemForm,UpdateItemForm



#create item ad
def create_item(request):
    if request.user.is_donor:
        if request.method=='POST':
            form=DonateItemForm(request.POST)
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


    
            


def update_item(request, pk):
    item = get_object_or_404(Items, pk=pk)  # This ensures item exists or returns a 404
    if request.method == 'POST':
        form = UpdateItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.info(request, 'Your items info has updated.')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            # When form is invalid, re-render the page with form errors.
            context = {'form': form}
            return render(request, 'items/update_ad.html', context)
    else:
        form = UpdateItemForm(instance=item)
        context = {'form': form}
        return render(request, 'items/update_ad.html', context)

    
            
# def update_item(request,pk):
#     item=Items.objects.get(pk=pk)
#     if request.method=='POST':
#         form=UpdateItemForm(request.POST,instance=item)
#         if form.is_valid():
#             form.save()
#             #var=form.save(commit=False)
#             #var.user =request.user
#             #var.save()
#             messages.info(request,'Your items info has updated.')
#             return redirect('dashboard')
#         else:
#             messages.warning(request,'something wont wrong')
#     else:
#         form=UpdateItemForm(instance=item)
#         context={'form':form}
#         return render(request,'items/update_ad.html',context)

