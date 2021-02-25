from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    #return HttpResponse('<h1>shipra chutiya<h1>') #for strings we use httpresponse
    replace = {'name':'Anish', 'msg':'bhai hai!!'}
    return render(request, 'index.html', replace) #for files containg html code etc

def add(request):
    result = int(request.POST['first_number'])+int(request.POST['second_number'])
    return render(request, 'result.htm', {'result':result})
