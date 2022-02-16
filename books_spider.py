import scrapy


class booksSpider(scrapy.Spider):
    name = "books"
    start_urls =  ['http://books.toscrape.com/']
    

    def parse(self, response):
        
        books = response.xpath('*//li/article[@class="product_pod"]')
            
        for a in books:
            yield{
                'title':a.xpath('.//h3/a/text()').get(),  #ok
                'price':a.xpath('.//p[@class="price_color"]/text()').get(), #ok
                'link':a.xpath('.//h3/a[@href]').get(), #ok
                'img_link':a.xpath('.//div[@class="image_container"]/a[@href]/img[@class="thumbnail"]').get() #ok
                }
        
        next_pg = response.xpath('*//li[@class="next"]/a/@href').get()
        if next_pg:
            yield response.follow(url=next_pg, callback=self.parse)
