from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='ownerlogin')
def ownerhome(request):
    return render(request,'turfowner.html')
