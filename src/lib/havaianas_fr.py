import scrapy
import json
from lib.Base_Class import Base_Class


class Havaianas_fr(Base_Class):
    def __init__(self):
        super().__init__()
    name = "Havaianas_fr"
    process_id = "63f619776ecb79dbb7ab2794"

    base_url = "https://www.havaianas-store.com"

    start_urls = [
        "https://www.havaianas-store.com/fr/fr/femme-all?=&start=0&sz=5000",
        "https://www.havaianas-store.com/fr/fr/homme-all?=&start=0&sz=5000",
        "https://www.havaianas-store.com/fr/fr/enfants-all?=&start=0&sz=5000"
    ]

    def parse(self, response):
        products = response.css("a.link::attr(href)").getall()
        for product in products:
            yield scrapy.Request(self.base_url + product, callback=self.parse_product)

    def parse_product(self, response):
        variants = response.css(
            "button.swatch.swatch--color.productSwatchs__swatch.js-productSwatchs::attr(data-url)").getall()
        for variant in variants:
            yield scrapy.Request(variant, callback=self.parse_variant)

    def parse_variant(self, response):
        parsed = json.loads(response.body)
        if parsed["product"]["price"].get("type") == "range":
            priceContainer = parsed["product"]["price"]["max"]
        else:
            priceContainer = parsed["product"]["price"]
        try:
            category = parsed["product"]["pageTitle"].split(" | ")[0].split("  ")[1].replace(
                "-", " ").strip() if parsed["product"]["pageTitle"] != None else "Non renseigné"
        except:
            category = "Non renseigné"
        product = {
            "name": parsed["product"]["productName"],
            "ref": parsed["product"]["id"],
            "desc": parsed["product"]["shortDescription"],
            "images": [img["url"] for img in parsed["product"]["images"]["large"]],
            "price": priceContainer["list"]["value"] if priceContainer["list"] != None else priceContainer["sales"]["value"],
            "reducedPrice": priceContainer["sales"]["value"],
            "currency": "EUR",
            "url": self.base_url + parsed["product"]["selectedProductUrl"],
            "brand": "Havaianas",
            "from": self.process_id,
            "composition": parsed["product"]["composition"].replace("<br>", " ") if parsed["product"]["composition"] != None else "Non renseigné",
            "category": category,
        }
        if product["price"] == None:
            product["price"] = product["reducedPrice"]
        self.products.append(product)