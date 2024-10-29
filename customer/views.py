from django.shortcuts import render

# Create your views here.

def userhome(request):
    return render(request,'index.html')


