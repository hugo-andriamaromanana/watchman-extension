import scrapy
import json
from lib.Base_Class import Base_Class

class Steve_madden_india(Base_Class):
    def __init__(self):
        super().__init__()

    name = "Steve_madden_india"
    processId = "63d7f19ecea0ba7f1e5b726c"
    base_url = "https://smpim.stevemadden.in/pim/pimresponse.php?service=category&store=1"
    categories = [
        "womens-allwomens",
        "mens-allmens",
        "handbags-allhandbags",
    ]

    def start_requests(self):
        for category in self.categories:
            yield scrapy.Request(self.base_url + "&url_key=" + category+"&page=1", callback=self.parse)

    def parse(self, response):
        jsonResp = json.loads(response.text)
        for product in jsonResp["result"]["products"]:
            if product["image"] != "":
                self.products.append({
                    "name": product["name"],
                    "ref": product["item_code"],
                    "desc": product["description"],
                    "images": [product["image"]],
                    "price": float(product["price"]),
                    "reducedPrice": float(product["selling_price"]),
                    "url": "https://www.stevemadden.in/product/" + product["url_key"],
                    "brand": "Steve Madden",
                    "currency": "INR",
                    "from": self.processId,
                    "meta": {"ean": product["ean"], "sku": product["sku"]}
                })
        current_page = int(response.url.split("&page=")[1])
        if current_page != jsonResp["query"]["total_page"]:
            yield scrapy.Request(response.url.split("&page=")[0] + "&page=" + str(current_page + 1), callback=self.parse)
