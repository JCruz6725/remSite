from django.shortcuts import render

# Create your views here.


def index(request):
    content = {}
    return render(request, 'resume/index.html', content)
