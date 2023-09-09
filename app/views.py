from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.
def student(request):
    sfo=studentlogin()
    d={'sfo':sfo}
    if request.method=='POST':
        sfdo=studentlogin(request.POST)
        if sfdo.is_valid():
            return HttpResponse(str(sfdo.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render(request,'student.html',d)