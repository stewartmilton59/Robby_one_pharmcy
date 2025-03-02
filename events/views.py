from django.shortcuts import render
from .models import Image
from .models import Video

# Create your views here.
def eventsImages(request):
    images = Image.objects.all()
    return render(request, "events/eventsImages.html", {'images': images})

def eventsVideos(request):
    videos = Video.objects.all()
    return render(request, "events/eventsVideos.html", {'videos': videos})
