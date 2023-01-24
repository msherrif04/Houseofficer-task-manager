from django.db import models
import uuid

# Create your models here.
class Bed(models.Model):
    number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    ward = models.CharField(max_length=255)

    def __str__(self):
        return self.number

    class Meta:
        ordering = ['number']

class Task(models.Model):
    task = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    complete = models.BooleanField(default=False)
    bed = models.ForeignKey(Bed, on_delete = models.CASCADE, blank=True, null=True)

    
    def __str__(self):
        return self.task[0:50]

    class Meta:
        ordering = ['-updated']


