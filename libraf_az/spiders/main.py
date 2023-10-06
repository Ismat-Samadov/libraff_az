from urllib.parse import urljoin

import scrapy


class MainSpider(scrapy.Spider):
    name = "main"
    allowed_domains = ["libraff.az"]
    start_urls = ["https://www.libraff.az/kitab/page-1/"]

    def parse(self, response):
        for book in response.css('div.ut2-gl__item'):
            image_url = urljoin(response.url, book.css('div.ut2-gl__body a img.cm-image::attr(data-src)').get())
            name = book.css('div.ut2-gl__name a.product-title::text').get()
            if image_url:
                yield {
                    'image_urls': [image_url],
                    'name': name,
                }

        next_page = response.css('div.coveo-result-cell a.CoveoResultLink::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
