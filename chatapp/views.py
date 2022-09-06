from django.shortcuts import render

from .models import Friend,Profile

# Create your views here.
def index(request):
    user = request.user.profile
    Friends = user.friends.all()
    context={'user':user,"friends":Friends}
    print(len(Friends))
    return render(request,"mychatapp/index.html", context)



def details(request, pk):
    friend = Friend.objects.get(profile_id = pk)
    context = {"friends":friend}
    return render(request,"mychatapp/details.html", context)