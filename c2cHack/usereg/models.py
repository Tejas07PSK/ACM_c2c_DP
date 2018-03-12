from django.db import models
import datetime
import random

# Create your models here.

def generateId():
    return random.randint(1,50)*3


class UserDetails(models.Model):
    usr_id = models.IntegerField(null=False, default=generateId(), primary_key=True, unique=True)
    fst_name = models.CharField(max_length=65, null=False)
    lst_name = models.CharField(max_length=65, null=False)
    eml = models.CharField(max_length=50, null=False, unique=True)
    pss = models.CharField(max_length=12, null=False, unique=True)

    def _str_(self):
        return (self.usr_id+'\n'+self.fst_name+'\n'+self.lst_name+'\n'+self.eml+'\n'+self.pss)





