import scrapy
import json
from FloatSpiderProject.items import FloatspiderprojectYoutubeItem
class YoutubeSpiderSpider(scrapy.Spider):
    name = 'youtube_spider'
    allowed_domains = ['www.googleapis.com']
    yt_API_key = 'AIzaSyCG5DYtT38m_Ia_NAlY6ZCxOwRUOL91GT8'
    videos_amount = 50
    start_urls = f'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode=TW&maxResults={videos_amount}&key=AIzaSyCG5DYtT38m_Ia_NAlY6ZCxOwRUOL91GT8'

    def start_requests(self):
        yield scrapy.Request(url=self.start_urls, callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        })
    def parse(self, response):
        Dictionary=json.loads(response.body)
        for item in Dictionary['items']:
            data={'channelTitle':item['snippet']['channelTitle'],
                  'title':item['snippet']['title'],
                  'thumbnails':item['snippet']['thumbnails']['standard']['url'],
                  'publishedAt': item['snippet']['publishedAt'],
                  'description':item['snippet']['description'],
                  'videosId':item['id']}
            channel_id=item['snippet']['channelId']
            banner_url =f'https://www.googleapis.com/youtube/v3/channels?part=snippet&id={channel_id}&fields=items%2Fsnippet%2Fthumbnails&key={self.yt_API_key}'
            yield scrapy.Request(
                url=response.urljoin(banner_url),
                callback=self.get_channel_banner,
                dont_filter=True,
                meta=data
            )

    def get_channel_banner(self,response):
        Dictionary = json.loads(response.body)
        response.request.meta['channelIconUrl']=Dictionary['items'][0]['snippet']['thumbnails']['default']['url']
        videos_id=response.request.meta['videosId']
        view_count_url =f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={videos_id}&key={self.yt_API_key}'
        yield scrapy.Request(
            url=view_count_url,
            callback=self.get_view_count,
            dont_filter=True,
            meta=response.request.meta
        )

    def get_view_count(self,response):
        Dictionary = json.loads(response.body)
        response.request.meta['viewCount'] =Dictionary['items'][0]['statistics']['viewCount']
        item = FloatspiderprojectYoutubeItem()
        item['channelTitle'] = response.request.meta['channelTitle']
        item['title'] = response.request.meta['title']
        item['thumbnails'] = response.request.meta['thumbnails']
        item['publishedAt'] = response.request.meta['publishedAt']
        item['description'] = response.request.meta['description']
        item['videosId'] = response.request.meta['videosId']
        item['channelIconUrl'] = response.request.meta['channelIconUrl']
        item['viewCount'] = response.request.meta['viewCount']
        yield item




