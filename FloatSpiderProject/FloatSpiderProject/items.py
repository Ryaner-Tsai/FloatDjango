# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy_djangoitem import DjangoItem
from bubbles.models import Ettoday
from bubbles.models import Youtube

class FloatspiderprojectItem(DjangoItem):
     django_model = Ettoday

class FloatspiderprojectYoutubeItem(DjangoItem):
     django_model = Youtube
