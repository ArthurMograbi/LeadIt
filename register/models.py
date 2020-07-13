
from django.db import models


class Vector(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    password= models.CharField(max_length=50)
    code = models.CharField(max_length=7)
    balanca = models.IntegerField(default=0)
    cnum = models.IntegerField(default=0)
    join_date = models.DateTimeField('date published')
    def __str__(self):
        return self.name


class Client(models.Model):
    papi = models.ForeignKey(Vector, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=80,default="NC")
    email = models.CharField(max_length=80,default="NC")
    join_date = models.DateTimeField('date published')
    kids = models.IntegerField(default=0)
    code = models.CharField(max_length=7)
    age = models.CharField(default=18,max_length=3)
    cpf = models.CharField(default="NC",max_length=20)
    cel = models.CharField(default="NC",max_length=20)
    vgen = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    def add_value(self,v,new=False):
        self.papi.balanca = self.papi.balanca+ v
        self.vgen = self.vgen+ v
        if new:
            self.papi.cnum = self.papi.cnum +1
        self.papi.save()
        self.save()
        return self.papi.cnum
