from django.db import models


class Employee(models.Model):
    picture = models.ImageField(upload_to='employees', null=True, blank=False)
    name = models.CharField(max_length=100)
    job_position = models.CharField(max_length=100)
    age = models.IntegerField()
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.name
