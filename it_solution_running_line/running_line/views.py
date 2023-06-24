from django.shortcuts import render, redirect
from .forms import TextForm


def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            text_value = form.cleaned_data['text']
            print(text_value)
            duration_value = form.cleaned_data['duration']
            print(duration_value)
            weight_value = form.cleaned_data['weight']
            print(weight_value)
            height_value = form.cleaned_data['height']
            print(height_value)
            return render(request, 'thankyou.html')
    else:
        form = TextForm()
    return render(request, 'index.html', {'form': form})


def thankyou(request):
    return render(request, 'thankyou.html')


