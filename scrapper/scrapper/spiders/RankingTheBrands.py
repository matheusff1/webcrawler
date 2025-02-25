import scrapy


class RankingthebrandsSpider(scrapy.Spider):
    name = "RankingTheBrands"
    allowed_domains = ["rankingthebrands.com"]
    start_urls = ["https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter=A"]

    def parse(self, response):
        
            for brand in response.css('#ctl00_mainContent_brandPanel .brandLine'):
                brand_name = brand.css('a span.rankingName::text').get()

            
                yield {
                    'name': brand_name,
                    'letter': 'a',
                }
