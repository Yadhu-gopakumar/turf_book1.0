from django.shortcuts import render
from turfowner.models import turf_table
# Create your views here.

def userhome(request):
    return render(request,'index.html')


def viewturflist(request):
    turfs = turf_table.objects.all()
    return render(request, 'viewturflist.html', {'turfs': turfs})

def searchturf(request):
    if 'query' in request.GET:
        q=request.GET['query']
        # uname=User.objects.filter(username__icontains=q)

        res=turf_table.objects.filter(name__icontains=q) | turf_table.objects.filter(location__icontains=q) 
   
        if res is not None:
            context={
                'turfs':res,
                    }
        else:
            context={
            'turfs':res,
                }  
        return render(request,'viewturflist.html',context)
    
def turfdetails(request,id):
    turf=turf_table.objects.get(id=id)
    return render(request,'turfdetails.html',{'turf':turf})

