from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from .models import Employee, BettingArea
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
    return HttpResponseRedirect("/employees/list/")


def employees_add_or_edit(request, employee_id):
    if employee_id == 0:
        employee = Employee.objects.create()
        context = {'employee': employee}
        html_form = render_to_string(
            'mainsite/employeeModalHolder.html',
            context,
            request=request,
        )
    else:
        employee_to_edit = Employee.objects.get(id=employee_id)
        context = {'employee': employee_to_edit}
        html_form = render_to_string(
            'mainsite/employeeModalHolder.html',
            context,
            request=request,
        )
    return JsonResponse({'html_form': html_form})


def employees_delete(request, employee_id):
    if request.method == 'POST':
        employee_to_delete = Employee.objects.get(id=employee_id)
        employee_to_delete.delete()
    else:
        print('request method in delete is not post')
    return employees_list(request)


def betting_areas_list(request):
    betting_areas = BettingArea.objects.all()
    context = {'betting_areas': betting_areas}
    return render(request, 'mainsite/machineList.html', context)
