
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Student,Myform
# Create your views here.
def home(request):
    members=Student.objects.all().values()
    return render(request,"disp.html",{'members':members})

def create(request):
    if request.method=='POST':
        form=Myform(request.POST)
        if form.is_valid():
            form.save()
        
        return HttpResponseRedirect('/myapp/home/')
    else:
        return render(request,"sample.html",{'form':Myform()})

def start(request):
    return render(request,"start.html",{})
