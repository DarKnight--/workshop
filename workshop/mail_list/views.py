from django.shortcuts import render
from django.utils import timezone
from .forms import ContactForm
from .forms import TeamRegistrationForm


def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return render(request, 'thanks.html')
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

def code42day_registration(request):
    if request.method == 'POST':
        form = TeamRegistrationForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return render(request, 'thanks.html')
    else:
        form = TeamRegistrationForm()
    return render(request, 'code42day_registration.html', {'form': form})