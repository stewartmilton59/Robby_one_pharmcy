from django.db import models

class Branch(models.Model):
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='branches/')
    description = models.TextField()

    def __str__(self):
        return self.location
