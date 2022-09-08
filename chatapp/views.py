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
    recieved_chats = chat_mes.objects.filter(msg_sender=reciever_id, msg_reciever=user_id, seen=False)
    recieved_chats.update(seen = True)



    if request.method == 'POST':
        form1 = MessageForm(request.POST)
        if form1.is_valid():
            chat_mesage = form1.save(commit=False)
            chat_mesage.msg_sender = user_id
            chat_mesage.msg_reciever = reciever_id
            chat_mesage.save()
            return redirect("detail", pk=friend.profile.id)
    context = {"friends":friend,"form":form,"user":user_id,"reciever":reciever_id, "chats":chats,"number1":recieved_chats.count()}
    return render(request,"mychatapp/details.html", context)


def base(request):
    return render(request, 'mychatapp/base.html')    




def sendMessage(request,pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id = friend.profile.id)
    data = json.loads(request.body)
    newchat=data["message1"]
    newchat_mesage = chat_mes.objects.create(message=newchat, msg_sender=user, msg_reciever=profile, seen=False)
    print(newchat)
    return JsonResponse(newchat_mesage.message, safe=False)



def recieveMessage(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id= friend.profile.id)
    arr =[]
    chats = chat_mes.objects.filter(msg_sender=profile, msg_reciever=user)
    for x in chats:
        arr.append(x.message)
    return JsonResponse(arr, safe=False)

def chatNotification(request):
    user = request.user.profile
    friends = user.friends.all()
    array1 = []
    for i in friends:
      chat  = chat_mes.objects.filter(msg_sender__id = i.profile.id, msg_reciever = user, seen =False )
      array1.append(chat.count())

    print(array1)

    return JsonResponse(array1, safe=False)
