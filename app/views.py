from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *

# Create your views here.
def students(request):
    sfo=studentlogin()
    d={'sfo':sfo}
    if request.method=='POST':
        sfdo=studentlogin(request.POST)
        if sfdo.is_valid():
            """sn=sfdo.cleaned_data['sname']
            si=sfdo.cleaned_data['sid']
            sa=sfdo.cleaned_data['sage']
            se=sfdo.cleaned_data['semail']
            so=student.objects.get_or_create(sname=sn,sid=si, sage=sa, semail=se)[0]
            so.save()
            sdo=student.objects.all()
            d={'sdo':sdo}"""
            #return render(request, 'display.html',d)
            return HttpResponse(str(sfdo.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render(request,'student.html',d)