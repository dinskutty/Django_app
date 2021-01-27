from django import forms
from myapp.models import Employee
class EmpForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields="__all__"

#student form
class StudentForm(forms.Form):  
    firstname = forms.CharField(label="Enter first name",max_length=50)  
    lastname  = forms.CharField(label="Enter last name", max_length = 100)