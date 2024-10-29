from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

def paymenthistory(request):
    return render(request,'paymenthistory.html')

def Turfowner(request):
    return render(request,'Turfowne.html')