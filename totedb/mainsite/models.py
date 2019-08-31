from django.db import models

# Create your models here.
        

class BettingArea(models.Model):
    area_name = models.CharField(max_length=20)


class Employee(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)


class Note(models.Model):
    note = models.CharField(max_length=1000)
    date = models.DateTimeField()
    

class Machine(models.Model):
    lsn_number = models.IntegerField()
    betting_area = models.IntegerField()
    serial_number = models.BigIntegerField()
    notes = models.ManyToManyField(Note, through='MachineNote')
    
  
class MachineNote(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    note = models.ForeignKey(Note, on_delete=models.CASCADE)


    
