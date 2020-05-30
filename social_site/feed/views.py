from django.shortcuts import render


tweets = [{'name': 'Praveen','text':'This is my first tweet'},{'name': 'tc','text':'This is my second tweet'}]
# Create your views here.
def home(request):
    context = {'tweets': tweets}
    return render(request,"feed/home.html",context)