from django.shortcuts import render

# home page
def homepage(request):
    return render(request, "website/index.html")
    
def aboutPage(request):
    return render(request, "website/about.html")
