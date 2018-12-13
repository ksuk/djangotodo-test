from django.db import models
from django.utils import timezone
# Create your models here.

class Posting(models.Model):
    message = models.CharField(max_length=140, verbose_name="ToDo")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date")

    def __str__(self):
        return self.message
        
    