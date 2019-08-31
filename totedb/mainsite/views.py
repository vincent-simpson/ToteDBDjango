from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse
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
    instance = Employee.objects.get(pk=request.POST["id"])
    if request.method == 'POST':
        form = SaveEmployeeForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
        else:
            print('Form is invalid')
    else:
        print('Request method is not post')
    return employees_list(request)
    


def employees_edit(request, employee_id):
    employee_to_edit = Employee.objects.get(id=employee_id)
    context = {'employee': employee_to_edit}
    html_form = render_to_string(
        'mainsite/employeeModalHolder.html',
        context,
        request=request,
    )
    return JsonResponse({'html_form': html_form})
