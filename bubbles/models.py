from django.db import models
# Create your models here.


class Ettoday(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    url = models.TextField()
    img_url = models.TextField()
    news_time = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

    @classmethod
    def delete_repeat(self):
        for row in self.objects.all():
            if self.objects.filter(url=row.url).count() > 1:
                self.objects.filter(url=row.url)[0].delete()

class Youtube(models.Model):
    channelTitle = models.CharField(max_length=255)
    title = models.TextField()
    thumbnails = models.TextField()
    publishedAt = models.CharField(max_length=255, default='')
    description = models.TextField()
    videosId = models.CharField(max_length=255, default='')
    channelIconUrl = models.TextField()
    viewCount = models.IntegerField()

    def __str__(self):
        return self.title

    @classmethod
    def delete_repeat(self):
        for row in self.objects.all():
            if self.objects.filter(videosId=row.videosId).count() > 1:
                self.objects.filter(videosId=row.videosId)[0].delete()

    def summary_title(self):
        if len(self.title)>35:
            return self.title[:35]+'...'
        else:
            return self.title

    def summary_description(self):
        return self.description[:100]+'...'
    @property
    def url(self):
        return 'https://www.youtube.com/watch?v='+self.videosId

