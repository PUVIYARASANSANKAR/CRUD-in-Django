from django.db import models

# Create your models here.
class Data(models.Model):
    Name=models.CharField(max_length=150,null=False,blank=False)
    Age=models.IntegerField(null=False,blank=False)
    Email=models.EmailField(max_length=150,null=False,blank=False)

    def __str__ (self):
        return('%s %s %s')%(self.Name,self.Age,self.Email)  