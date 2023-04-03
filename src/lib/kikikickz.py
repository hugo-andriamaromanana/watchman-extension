import scrapy
import chompjs
from lib.Base_Class import Base_Class

class Kikikickz(Base_Class):
    def __init__(self):
        super().__init__()
    name = "Kikikickz"
    processId = "63be8fc4bc73f6d57c55bb52"
    start_urls = [
        "https://kikikickz.com/collections/all?page=1"
    ]
    base_url = "https://kikikickz.com"

    def parse(self, response):
        for product in response.css('a.product__item__link--container'):
            yield scrapy.Request(self.base_url + product.css('::attr(href)').extract_first(), callback=self.parseProduct)
        if response.css('a.product__item__link--container'):
            currentPage = response.url.split("page=")[1]
            newUrl = response.url.replace("page=" + currentPage, "page=" + str(int(currentPage) + 1))
            yield scrapy.Request(newUrl, callback=self.parse)
    def parseProduct(self, response):
        script = response.css("script[type='application/ld+json']::text").extract_first()
        parsed = chompjs.parse_js_object(script)
        for off in parsed["offers"]:
            product = {
                "name": parsed["name"],
                "ref": off["sku"],
                "desc": parsed["description"],
                "images": [parsed["image"]["url"]],
                "price": float(response.css("span.product--compare-at-price::text").extract_first().replace("€", "")),
                "reducedPrice": float(off["price"]),
                "url": response.url,
                "brand": parsed["brand"]["name"],
                "currency": "EUR",
                "from": self.processId
            }
            self.products.append(product)