from django.shortcuts import render
from lion.models import Lion, Identity

def main(request):
    lion = Lion.objects.all()
    return render(request, 'main.html', {'lion':lion})
    
    