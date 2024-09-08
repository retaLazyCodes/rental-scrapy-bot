import scrapy


class BuscaPropSpider(scrapy.Spider):
    name = "buscaprop"

    def start_requests(self):
        url = f"{self.settings.get('BUSCAPROP_URL')}{self.settings.get('BUSCAPROP_FILTER')}"

        if url:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response.status)
