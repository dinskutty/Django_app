from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
import datetime
from django.views.decorators.http import require_http_methods

#http decorator
@require_http_methods(["GET"])
def showpg(request):  
    return HttpResponse('<h1>This is Http GET request.</h1>')

# loading templates
from django.template import loader
def index(request):  
   template = loader.get_template('index.html') # getting our template  
   name={
       'student':'Dk','class':'MCA'
   }
   return HttpResponse(template.render(name))       # rendering the template in HttpResponse  

# Create your views here.
def myfn(request):
    return HttpResponse('<h2>This is my first Django project</h2>')
def index3(request):
    tim=datetime.datetime.now()
    html="<h3>Now Time is %s</h3>"%tim
    return HttpResponse(html)
def index2(request):
    a=1
    if a:
        return HttpResponseNotFound("<h2>Not found</h2>")
    else:
        return HttpResponse("<h2>page found</h2>")

#loading image using static
def imag(request):
    return render(request,'imag.html')
#loading js file using static
def js_file(request):
    return render(request,'script.html')