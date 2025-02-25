import scrapy


class RankingthebrandsSpider(scrapy.Spider):
    name = "RankingTheBrands"
    allowed_domains = ["rankingthebrands.com"]
    start_urls = ["https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx"]

    def parse(self, response):
        for index in response.css('ctl00_mainContent_filterPanel'):
            print(index)
            for brand in response.css('ctl00_mainContent_brandPanel'):
                print(brand)
                yield{
                    'index':index.css('::text').get(),
                    'name':brand.css('::text').get(),
                }
