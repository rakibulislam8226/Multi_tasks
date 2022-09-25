
from django.shortcuts import render, redirect
from pytube import YouTube
from django.contrib import messages

# Create View


def youtube(request):
    if request.method == 'POST':
        # getting link from frontend
        link = request.POST['link']
        video = YouTube(link)

        # setting video resolution
        stream = video.streams.get_highest_resolution()

        # downloads video
        stream.download()
        messages.success(request, 'Download Successfully!')
        return render(request, 'youtube.html')
    return render(request, 'youtube.html')
