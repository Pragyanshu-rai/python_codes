from django.shortcuts import render,get_object_or_404

from django.http import HttpResponse 
 
from .models import Question

# Create your views here.
def owner(request):
    return HttpResponse("Hello, world. 87da3a68 is the polls index.")

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'index.html', context)

#def index(request):
#    return HttpResponse('Answer to the Ultimate Question')

def detail(request, pk):
    question = get_object_or_404(Question, pk=pk)
    return render(request, 'detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def home(request):
    return HttpResponse('Home Page!!');

def new_page(request):
    response = '''
<html>
        <head>
            <title>Contact Page</title>
            <link rel="stylesheet" type="text/css" href="./bootstrap.css"/>
        <link rel="stylesheet" type="text/css" href="./style.css"/>
        </head>
        <body>
		    <a href="./index.html">home</a>
		    &nbsp;
		    <a href="./aboutme.html">about_me</a>
		    &nbsp;
		    <a href="./contact.html">contact</a>
		    &nbsp;
		    <a href="./jqy.html">jqy</a>
		    &nbsp;
		    <a href="./count.html">counter</a>
		    &nbsp;
		    <a href="./imggal.html">Image Gallery</a>
		    <hr/>
            <h1>Contact me page</h1>
            <p>hello!!!!!!!:)</p>
        </body>
</html>
    '''
    return HttpResponse(response)
