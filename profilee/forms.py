from django import forms 
from .models import Employee 
  
  
# creating a form 
class EmployeeForm(forms.ModelForm): 

    # create meta class 
    class Meta: 
        # specify model to be used 
        model = Employee
        # specify fields to be used 
        fields = [ 
            "Manager",
            "empid", 
            "fname", 
            "lname", 
            "address", 
            "DOB", 
            "mob",
            "city", 
        ] 