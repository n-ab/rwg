from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
def index(request):
    unique_id = get_random_string(length=15)
    context = {
    "randomword" : unique_id

    }
    return render(request, 'rwg/index.html', context)
# Create your views here.
