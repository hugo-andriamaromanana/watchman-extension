import scrapy
import json
from lib.Base_Class import Base_Class


class TheBradery(Base_Class):
    def __init__(self):
        super().__init__()
    name = "The Bradery"
    processId = "63821ac7b3353ff3a8cc7ce5"
    start_urls = [
        "https://thebradery.com/collections"
    ]

    def parse(self, response):
        ahrefs = response.css('a::attr(href)').extract()
        paths = [x for x in ahrefs if x.startswith("/collections/")]
        paths = list(set(paths))
        for path in paths:
            yield scrapy.Request(response.urljoin(path + "/products.json?view=metafields&limit=100000&page=1"), callback=self.parse_category)

    def parse_category(self, response):
        products = json.loads(response.body)
        for product in products["products"]:
            for sku in product["variants"]:
                if sku["sku"] != "" and sku["sku"] is not None:
                    self.products.append({
                        "name": product["title"],
                        "ref": sku["sku"],
                        "desc": product["body_html"],
                        "images": [x["src"] for x in product["images"]],
                        "price": float(product["variants"][0]["compare_at_price"] or product["variants"][0]["price"]),
                        "reducedPrice": float(product["variants"][0]["price"]),
                        "url": "https://thebradery.com/products/"+product["handle"],
                        "brand": product["vendor"],
                        "currency": "EUR",
                        "category": product["product_type"],
                        "meta": {},
                        "from": self.processId,
                    })
