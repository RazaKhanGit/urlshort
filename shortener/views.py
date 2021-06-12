from django.http.response import HttpResponse
from .forms import customURL, urlForm
from .models import URLData
from django.shortcuts import render, redirect
from django.http import HttpResponse 
import random
import string

# Create your views here.
def home(request):
    all_urls = URLData.objects.all()
    full_url = request.build_absolute_uri(None)
    return render(request, 'home.html', {'all_urls': all_urls, 'full_url': full_url})

def urlShortener(request):
    if request.method == 'POST':
        form = urlForm(request.POST)
        if form.is_valid():
            slug = ''.join(random.choice(string.ascii_letters) for x in range(10))
            url = form.cleaned_data["url"]
            new_url = URLData(url=url, slug=slug)
            new_url.save()
            return redirect('/')
    else:
        form = urlForm()
    return render(request, 'form.html', {'form':form})

def urlCustom(request):
    if request.method == 'POST':
        form = customURL(request.POST)
        if form.is_valid():
            slug = form.cleaned_data["slug"]
            url = form.cleaned_data["url"]
            try:
                check_url = URLData.objects.get(slug=slug)
            except URLData.DoesNotExist:
                check_url = None
            if check_url != None:
                return HttpResponse("Slug already taken!!!")
            new_url = URLData(url=url, slug=slug)
            new_url.save()
            return redirect('/')
    else:
        form = customURL()
    return render(request, 'form.html', {'form':form})

def urlRedirect(request, slug):
    data = URLData.objects.get(slug=slug)
    return redirect(data.url)