from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

'''
 django model field : 
    - html widget
    - validation 
    - db size 
'''

JOB_TYPE = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time'),
)

def image_upload(instance,filename):
    imagename , extension = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)



class Job(models.Model):  # table 
    title = models.CharField(max_length=100)  # column