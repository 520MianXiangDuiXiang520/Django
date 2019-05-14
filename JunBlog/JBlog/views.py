from django.shortcuts import render
from .models import Topmeau

# Create your views here.
def index(requests):
    topmeau=Topmeau.objects.all()
    context={
        'topmeau':topmeau
    }
   
    return render(requests,'Blog/blog.html',context)