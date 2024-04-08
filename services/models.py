from django.db import models

class Service(models.Model):
    image = models.ImageField(upload_to='services', null=True, blank=False)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.title
