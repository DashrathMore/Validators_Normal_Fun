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
            sn=sfdo.cleaned_data['s_name']
            si=sfdo.cleaned_data['s_id']
            sa=sfdo.cleaned_data['s_age']
            se=sfdo.cleaned_data['s_Email']
            so=student.objects.get_or_create(sname=sn,sid=si, sage=sa, semail=se)[0]
            so.save()
            sdo=student.objects.all()
            d={'sdo':sdo}
            return render(request, 'display.html',d)
        else:
            return HttpResponse('Invalid data')
    return render(request,'student.html',d)