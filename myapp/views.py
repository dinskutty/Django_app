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
#loading css file using static
def cs(request):
    return render(request,'cs.html')

#loading model form
from myapp.form import EmpForm

def inde(request):
    emp=EmpForm()
    return render(request,"inde.html",{'form':emp})


from myapp.form import StudentForm  
  
def inde2(request):  
    student = StudentForm()  
    return render(request,"inde.html",{'form':student})  

#django validation
def emp(request):  
    if request.method == "POST":  
        form = EmpForm(request.POST)  
        if form.is_valid():  
            try:  
                return redirect('/')  
            except:  
                pass  
    else:  
        form = EmpForm()  
    return render(request,'inde.html',{'form':form})

#file upload
from myapp.functions.functions import handle_uploaded_file
from myapp.form import StudForm 
def filep(request):  
    if request.method == 'POST':  
        student = StudForm(request.POST, request.FILES)  
        if student.is_valid():  
            handle_uploaded_file(request.FILES['file'])  
            return HttpResponse("File uploaded successfuly")  
    else:  
        student = StudForm()  
        return render(request,"inde.html",{'form':student}) 

#creating csv with django
import csv
def getfile(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="file.csv"'
    writer = csv.writer(response)  
    writer.writerow(['1001', 'John', 'Domil', 'CA'])  
    writer.writerow(['1002', 'Amit', 'Mukharji', 'LA', '"Testing"'])  
    return response 

#dynamic csv using django
from myapp.models import Employee
def getdt(request):
    response=HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment;filename="file2.csv"'
    employees= Employee.objects.all()
    writer =csv.writer(response)
    for employee in employees:
        writer.writerow([employee.first_name,employee.last_name,employee.mbl])
    return response

#using pdf in django
from reportlab.pdfgen import canvas
def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="sampl.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "my first pdf creaton")  
    p.showPage()  
    p.save()  
    return response 

#bootstrap
def boot(request):
    return render(request,'boots.html')

#setting up mails
from djangoapp import settings
from django.core.mail import send_mail

def mails(request):
    sub="Greetings"
    msg="Congratulations for your success  dear lusu!! :)"
    to="saidharanisai143@gmail.com"
    res=send_mail(sub,msg,settings.EMAIL_HOST_USER,[to])
    if(res==1):
        msg="Mail sent successfully"
    else:
        "Mail could not sent"
    return HttpResponse(msg)