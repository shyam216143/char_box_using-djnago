from django.shortcuts import render
import threading
# Create your views here.

def index(request):
    print(threading.get_native_id())
    return render(request, 'chat/index.html')



def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })