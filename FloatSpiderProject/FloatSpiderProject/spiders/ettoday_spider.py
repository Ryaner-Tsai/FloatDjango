import scrapy
from FloatSpiderProject.items import FloatspiderprojectItem

class EttodaySpiderSpider(scrapy.Spider):
    name = 'ettoday_spider'
    allowed_domains = ['www.ettoday.net']
    def start_requests(self):
        yield scrapy.Request(url='https://www.ettoday.net/news/hot-news.htm', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        })
    def parse(self, response):
        #1.取得selectors→2.將selector的資訊篩選出來存入一個字典(測試:可不可以yield兩個以上)→3.創造一個新formrequest，callback:after_first_page並將字典存進meta
        #4.進入after_first_page後取得selector→5.篩選所需，存入字典→6.若新聞未超過100個，則callback自己
        for new_selector in response.xpath('//div[@class="part_pictxt_3"]/div[@class="piece clearfix"]'):
            item = FloatspiderprojectItem()
            item['title']=new_selector.xpath('.//h3/a/text()').get()
            item['summary'] = new_selector.xpath('.//p/text()').get()
            item['news_time'] = response.urljoin(new_selector.xpath('.//span/text()').get())
            item['url'] = response.urljoin(new_selector.xpath('.//a/@href').get())
            item['img_url'] = response.urljoin(new_selector.xpath('.//a/img/@data-original').get())
            yield item

            # yield response.follow(url=link,callback=self.parseNewsDeatil, meta={'title': NewSelector.xpath('.//a/text()').get(),'time': NewSelector.xpath('.//span/text()').get(),
            #                                                                     'kind': NewSelector.xpath('.//em/text()').get(),'link': response.urljoin(NewSelector.xpath('.//a/@href').get())})
        #3.取得各連結response，並且取得其中的圖片(1.rule1&rule2)(2.利用meta)(3.再傳request)
            #3.1
    # def parseNewsDeatil(self,response):
    #
    #     imgLink = response.xpath('(//div[@class="story"]/descendant::node()/img)[1]/@src').get()
    #     yield {
    #         'title':response.request.meta['title'],
    #         'time': response.request.meta['time'],
    #         'kind': response.request.meta['kind'],
    #         'link': response.request.meta['link'],
    #         'imgLink':imgLink}
        #1.取200個:a.透過detail callback b. yield 兩個，一個是response.follow；另一個是formrequest