from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=200, null=False)
    bio = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
