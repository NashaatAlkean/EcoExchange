from django.shortcuts import render,get_object_or_404,redirect
from items.models import Items
from .models import Conversation
from .forms import ConversationMessageForm
from django.contrib.auth.decorators import login_required

@login_required
def new_conversation(request,item_pk):
    item=get_object_or_404(Items,pk=item_pk)

    if item.user==request.user:
        return redirect('home')
    
    conversation=Conversation.objects.filter(item=item).filter(members__in=[request.user.id])

    if conversation:
        #if alreday conversation exist
        pass

    if request.method=='POST':
        form=ConversationMessageForm(request.POST)
        if form.is_valid():
                conversation=Conversation.objects.create(item=item)
                conversation.members.add(request.user)
                conversation.members.add(item.user)
                conversation.save()
                conversation_message=form.save(commit=False)
                conversation_message.conversation=conversation
                conversation_message.created_by=request.user
                conversation_message.save()

                return redirect('item-details',pk=item_pk)
    else:
         form=ConversationMessageForm()
    
    
    
    return render(request,'conversation/new_conv.html',{'form':form})


@login_required

def inbox(request):
    conversation=Conversation.objects.filter(members__in=[request.user.id])

    return render(request,'conversation/inbox.html',{'conversation':conversation})


@login_required
def detail(request, pk):
    conversation = get_object_or_404(Conversation, members__in=[request.user.id], pk=pk)

    if request.method == 'POST':
        form = ConversationMessageForm(request.POST)
        if form.is_valid():
            conversation_message = form.save(commit=False)
            conversation_message.conversation = conversation
            conversation_message.created_by = request.user
            conversation_message.save()
            return redirect('conversation:detail', pk=pk)
    else:
        form = ConversationMessageForm()

    return render(request, 'conversation/detail.html', {
        'conversation': conversation,
        'form': form
    })
