from django.http import HttpResponse
from django.shortcuts import render

def blog(request):
    #return HttpResponse('blog')
    return render(request, 'blog.html')

def onas(request):
    #return HttpResponse('onas')
    return render(request, 'onas.html')