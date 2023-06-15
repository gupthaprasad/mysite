from django.db import models

class Student(models.Model):
    fn=models.CharField(verbose_name="FirstName",max_length=100)
    ln=models.CharField(verbose_name="LastName",max_length=250)
    dob=models.DateField(verbose_name="DateOfBirth")
    def __str__(self):
        return self.fn+' '+self.ln
