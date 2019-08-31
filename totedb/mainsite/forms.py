from django.forms import ModelForm
from .models import Employee

class SaveEmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'phone_number']
        