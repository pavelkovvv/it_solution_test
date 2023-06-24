from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import TextForm
from .utils import create_video_with_text


def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            form.save()
            text_value = form.cleaned_data['text']
            duration_value = form.cleaned_data['duration']
            weight_value = form.cleaned_data['weight']
            height_value = form.cleaned_data['height']
            size_text_value = form.cleaned_data['size_text']
            create_video_with_text(text_value, duration_value, weight_value,
                                   height_value, size_text_value)
            return redirect('running_line:download_video')
    else:
        form = TextForm()
    return render(request, 'index.html', {'form': form})


def download_video(request):
    video_path = "output.mp4"

    with open(video_path, 'rb') as video_file:
        response = HttpResponse(video_file.read(), content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename="video.mp4"'
        return response



