from email.quoprimime import body_check
import json
import profile
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Friend,Profile,chat_mes
from .form import MessageForm
# Create your views here.
def index(request):
    user = request.user.profile
    Friends = user.friends.all()
    context={'user':user,"friends":Friends}
    print(len(Friends))
    return render(request,"mychatapp/index.html", context)



def details(request, pk):
    friend = Friend.objects.get(profile_id = pk)
    form   = MessageForm()
    user_id = request.user.profile
    reciever_id = Profile.objects.get(id = friend.profile.id)
    chats = chat_mes.objects.all()
    print(chats[0])


    if request.method == 'POST':
        form1 = MessageForm(request.POST)
        if form1.is_valid():
            chat_mesage = form1.save(commit=False)
            chat_mesage.msg_sender = user_id
            chat_mesage.msg_reciever = reciever_id
            chat_mesage.save()
            return redirect("detail", pk=friend.profile.id)
    context = {"friends":friend,"form":form,"user":user_id,"reciever":reciever_id, "chats":chats}
    return render(request,"mychatapp/details.html", context)


def base(request):
    return render(request, 'mychatapp/base.html')    




def sendMessage(request,pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id= friend.profile.id)
    data = json.loads(request.body)
    newchat=data["message1"]
    newchat_mesage = chat_mes.objects.create(message=newchat, msg_sender=user, msg_reciever=profile, seen=False)
    print(newchat)
    return JsonResponse(newchat_mesage, safe=False)