from multiprocessing import context
from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required

def home(request):
    threads = ThreadingTable.objects.by_user(user=request.user).prefetch_related('message1').order_by('timestamp')
    context={
        'threads':threads,
    }
    return render(request,"message.html", context)