from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(default="test@example.com")
    languages = models.TextField(default="English")
    premium = models.BooleanField(default=False)
