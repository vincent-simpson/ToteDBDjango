from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', include([
        path('list/', views.employees_list, name='employee_list'),
        path('save/', views.employees_save, name="employee_save"),
        path('delete/<int:employee_id>/', views.employees_delete, name="employee_delete"),
        path('add/<int:employee_id>/', views.employees_add_or_edit, name='employee_add'),
    ])),
    path('bettingAreas/', include([
        path('list/', views.betting_areas_list, name="betting_areas_list"),
    ])),
]