from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', include([
        path('list/', views.employees_list, name='employee_list'),
        path('edit/<int:employee_id>/', views.employees_edit, name="employee_edit"),
        path('save/', views.employees_save, name="employee_save"),
    ]))
]