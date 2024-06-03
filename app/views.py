from django.shortcuts import render
from app.models import *
# Create your views here.
from app.forms import *
from django.http import HttpResponse
from django.core.mail import send_mail

def registation(request):
    EUFO=UserForm()
    EPFO=ProfileForm()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=='POST' and request.FILES:
        NMUFDO=UserForm(request.POST)
        NMPFDO=ProfileForm(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            MUFDO=NMUFDO.save(commit=False)
            PW=NMUFDO.cleaned_data['password']
            MUFDO.set_password(PW)
            MUFDO.save()


            MPFDO=NMPFDO.save(commit=False)

            MPFDO.username=MUFDO
            MPFDO.save()



            send_mail('Registation',
                      'thaks for registation',
                      'kiranprabhu@gmail.com',
                      [MUFDO.email],
                      fail_silently=True

            )
        
            return HttpResponse('registation is successfull')
        else:
            return HttpResponse('invalid data')









    return render(request,'registation.html',d)