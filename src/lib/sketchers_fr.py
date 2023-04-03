import scrapy
import os
from lib.Base_Class import Base_Class


class Sketchers_fr(Base_Class):
    def __init__(self):
        super().__init__()
    name = "Sketchers_fr"

    url = "https://www.skechers.fr"
    process_id = "63f38f1ae8021ab1d4304c35"

    custom_settings = {
        'DOWNLOAD_DELAY': 8,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
    }

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36",
    }

    with open(os.path.join(os.path.dirname(__file__), "confs/sketchers.txt"), "r") as f:
        raw = f.read()
        categories = raw.split("\n")

    def start_requests(self):
        for category in self.categories:
            yield scrapy.Request(self.url + category + "?start=0&sz=3000", callback=self.parse, headers=self.headers, meta={"category": category},)

    def parse(self, response):
        productsUrls = response.css(
            "a.c-product-tile__color-swatches__swatch.js-swatch-hover::attr(href)").getall()
        for productUrl in productsUrls:
            yield scrapy.Request(self.url + productUrl, callback=self.parse_product, headers=self.headers, meta=response.meta)

    def parse_product(self, response):
        images = response.css(
            "div.c-pdp-carousel__thumbnails__container img::attr(src)").getall()
        images = [image.split("?")[0] for image in images]
        prices = response.css(
            "span.price__inner span.value::attr(content)").getall()
        category = response.meta["category"].replace("/", " ").strip()
        color = response.css(
            "span.js-product-details-attr-colorCode.c-product-attributes__item__selected-val.c-product-attributes__item__selected-val--color::text").get().strip()
        product = {
            "name": response.css("h1.product-name::text").get(),
            "ref": response.css("span.product-id::text").get().strip() + " "+response.css("span.js-product-details-color-colorCode::text").get().strip(),
            "desc": response.css("div.c-product-details__overview::text").get().strip() if response.css("div.c-product-details__overview::text").get() else "",
            "images": images,
            "price": float(prices[0]),
            "reducedPrice": float(prices[-1]),
            "url": response.url,
            "brand": "Sketchers",
            "from": self.process_id,
            "currency": "EUR",
            "category": category,
            "color": color,
        }
        self.products.append(product)
