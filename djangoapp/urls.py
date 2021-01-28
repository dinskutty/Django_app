"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myurl/', views.myfn),
    path('date/',views.index3),
    path('pag/',views.index2),
    path('show/',views.showpg),
    path('index/', views.index), 
    path('image/',views.imag),
    path('js/',views.js_file),
    path('cs/',views.cs),
    path('forms/',views.inde),
    path('forms2/',views.inde2),
    path('validat/',views.emp),
    path('upload/',views.filep),
    path('csv/',views.getfile),
    path('csvs/',views.getdt),
    path('getpdf/',views.getpdf),
    path('bootsrp/',views.boot),
    path('mail/',views.mails),
]
