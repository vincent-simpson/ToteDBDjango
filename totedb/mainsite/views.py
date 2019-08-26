from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from .forms import SaveEmployeeForm

# Create your views here.

def index(request):
    return render(request, template_name='mainsite/index.html')


def employees_list(request):
    employee_list = Employee.objects.all()
    context = {'employee_list': employee_list}
    return render(request, 'mainsite/employeeList.html', context)


def employees_save(request):
    form = SaveEmployeeForm(request.POST or None)
    if(form.is_valid()):
        form.save()
    
    return employees_list(request)


def employees_edit(request, employee_id):
    employee_to_edit = Employee.objects.get(id = employee_id)
    return HttpResponse(employee_to_edit)
    

