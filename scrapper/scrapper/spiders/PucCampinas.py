import scrapy


class PuccampinasSpider(scrapy.Spider):
    name = "PucCampinas"
    allowed_domains = ["puc-campinas.edu.br"]
    start_urls = ["https://www.puc-campinas.edu.br/graduacao/"]

    def parse(self, response):
        for curso in response.css('.vc_gitem-link'):
            yield {
                "curso": curso.css("::text").get(),
            }
