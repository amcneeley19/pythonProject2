from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'EatIt/index.html')
def search(request):
    return render(request, 'EatIt/search.html')
