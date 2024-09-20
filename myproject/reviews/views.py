from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import review


def home(request):
    return render(request, 'reservations/home.html')


def review_form(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()     
    else:
        form = ReviewForm()
    return render(request, 'reservations/review_form.html', {'form': form})