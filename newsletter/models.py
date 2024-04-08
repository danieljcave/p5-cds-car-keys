from django.db import models

class Newsletter(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    scheduled_send_date = models.DateField()
