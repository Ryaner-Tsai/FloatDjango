

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Ettoday
from .models import Youtube
from django.utils import timezone
import random

# Create your views here.
def home(request):
    Ettoday.delete_repeat()
    Youtube.delete_repeat()
    ettoday_news = Ettoday.objects
    youtube_videos = Youtube.objects
    combined_bubbles = []

    for post in ettoday_news.all():
        combined_bubbles.append(post)
    for post in youtube_videos.all():
        combined_bubbles.append(post)
    random.shuffle(combined_bubbles)
    print(combined_bubbles)

    # Ettoday.delete_repeat()
    return render(request, 'bubbles/home.html',{'combined_bubbles':combined_bubbles})