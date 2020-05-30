from django.shortcuts import render
from .models import tweet
from django.contrib.auth.decorators import login_required
from django.contrib.auth import user_logged_out
# Create your views here.

@login_required
def home(request):
    context = {'tweets': tweet.objects.all}
    return render(request,"feed/home.html",context)