from django.shortcuts import (render, get_object_or_404)
from django.http import HttpResponse
from .models import Reporter, Article
from django.views import View
#django.http import HttpResponse

from .forms import ReporterForms, ContactModel, ArticleModel

def add(request):
    form = ReporterForms(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            reporter = Reporter()
            reporter.first_name = request.POST.get('first_name')
            reporter.last_name = request.POST.get('last_name')
            reporter.email = request.POST.get('email')
            reporter.save()
            form.cleaned_data
            print(request.POST.get('title'))
    else:
        form = ReporterForms()
    return render(request, 'albums/add.html', {'Forms': form})


def model_add(request):
    form = ContactModel(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            print(request.POST)
            print('here')
            form.save()
    else:
        form = ContactModel()
    return render(request, 'albums/add.html', {'Forms': form})

def article_add(request):
    form = ArticleModel(request.POST or None)
    
    if request.method == "POST":
        if form.is_valid():
            print(request.POST)
            print('here')
            form.save()
    else:
        form = ArticleModel()
    return render(request, 'albums/add.html', {'Forms': form})

class add_form(View):
    def get(self, request, *args, **kwargs):
        form = ArticleModel()
        return render(request, "albums/add.html", {'Forms': form})

    def post(self, request, *args, **kwargs):
        form = ArticleModel(request.POST or None)
        print(request.POST.get('headline'))
        if form.is_valid():
            print(request.POST)
        else:
            return render(request, "albums/add.html", {'Forms': form})
