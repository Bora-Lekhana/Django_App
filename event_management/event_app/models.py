from django.db import models

class EventRegistration(models.Model):
    name = models.CharField(max_length=100)              
    password = models.CharField(max_length=128, default='default_password')
    email = models.EmailField()                           
    phonenumber = models.CharField(max_length=15, blank=True) 
    address = models.TextField(blank=True)                 
    eventname = models.CharField(max_length=100)       
    date = models.DateField()                              

    def __str__(self):
        return f"{self.name} - {self.eventname}"


