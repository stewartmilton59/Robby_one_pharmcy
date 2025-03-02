from django.db import models

class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled"

class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    video_file = models.FileField(upload_to="videos/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
