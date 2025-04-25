from django.shortcuts import render

def index(request):
    return render(request, 'index.html')  # This will render the 'index.html' template
