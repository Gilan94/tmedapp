from django.db import models
import datetime
import os

# Create your models here.

class Task(models.Model):
  title = models.CharField(max_length=200)
  gilan = models.TextField(max_length=200, null=True)
  completed = models.BooleanField(default=False, blank=True, null=True)
      
  def __str__(self):
    return self.title


def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('uploads/', filename)

class Item(models.Model):
    name = models.TextField(max_length=200)
    iin = models.IntegerField(null=True)
    tel_number = models.IntegerField( null=True)
    doctor = models.TextField(max_length=200, null=True)
    image = models.FileField(upload_to=filepath, null=True)
    client_type =  models.TextField(max_length=50, null=True)
    status = models.TextField(max_length=50, null=True)
    datetime = models.DateTimeField(max_length=50, null=True)
    link = models.TextField(max_length=2500, null=True)
