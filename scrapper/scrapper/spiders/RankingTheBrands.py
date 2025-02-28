import scrapy

from ..items import Brand


class RankingthebrandsSpider(scrapy.Spider):
    name = "RankingTheBrands"
    allowed_domains = ["rankingthebrands.com"]
    start_urls = ["https://www.rankingthebrands.com/The-Brands-and-their-Rankings.aspx?catFilter=0&nameFilter=A"]

    def parse(self, response):
        for option in response.css('#ctl00_mainContent_filterPanel a'):
            letter = option.css("::text").get()
            link = response.urljoin(option.attrib["href"])

            yield response.follow(link, callback=self.parse_brands, meta={"letter": letter})

    def parse_brands(self, response):
        letter = response.meta["letter"]

        for brand in response.css('#ctl00_mainContent_brandPanel .brandLine'):
            brand_name = brand.css('a span.rankingName::text').get()
            brand_x = Brand(name=brand_name, letter=letter)
            yield brand_x

