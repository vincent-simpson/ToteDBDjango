from django.contrib import admin
from .models import Employee, BettingArea, Machine, Note, MachineNote

admin.site.register([Employee, BettingArea, Machine, Note, MachineNote])

# Register your models here.
