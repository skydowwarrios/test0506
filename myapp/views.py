from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def hello(request):
    return HttpResponse('<h1>Hello world!</h1>')
    
def hello2(request,username):
    now = datetime.now()
    return render(request,'hello3.html',
                   {'username':username,'now':now})