from django.shortcuts import render

# Create your views here.
def home_view(request):
    """Display the home page view"""
    return render(request, 'home.html')