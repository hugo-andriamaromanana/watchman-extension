import scrapy
import chompjs
from lib.Base_Class import Base_Class


class Eastpak_fr(Base_Class):
    def __init__(self):
        super().__init__()

    name = "Eastpak_fr"
    process_id = "63e25cdd1b81cce088d6a998"

    base_urls = [
        "https://www.eastpak.com/fr-fr/sacs-a-dos-c120.html",
        "https://www.eastpak.com/fr-fr/bagages-c140.html",
        "https://www.eastpak.com/fr-fr/sacs-a-bandouliere-c130.html",
        "https://www.eastpak.com/fr-fr/accessoires-c150.html",
    ]

    def start_requests(self):
        for base_url in self.base_urls:
            yield scrapy.Request(base_url+"?p=1", callback=self.parse)

    def parse(self, response):
        script = response.css(
            "script:contains('staticImpressions')::text").get()
        script = script.replace(
            "var staticImpressions = staticImpressions || {};", "")
        script = script.replace(
            "staticImpressions['category.products.list'] = ", "")
        parsed = chompjs.parse_js_object(script)
        atags = response.css("a.product-item-link")
        for i in range(len(atags)):
            href = atags[i].attrib["href"]
            yield scrapy.Request(href, callback=self.parse_product, meta={"category": parsed[i]["category"]})

        if len(atags) != 0:
            new_url = response.url.split(
                "?p=")[0]+"?p="+str(int(response.url.split("?p=")[1])+1)
            yield scrapy.Request(new_url, callback=self.parse)

    def parse_product(self, response):
        ref = response.css(
            "form#product_addtocart_form").attrib["data-product-sku"]
        name = response.css("h1.page-title span::text").get()
        price = response.css("span.price::text").get().replace(
            "€", "").replace(",", ".")
        reducedPrice = response.css(
            "span.special-price span.price::text").get()
        if reducedPrice is None:
            reducedPrice = price
        else:
            reducedPrice = reducedPrice.replace("€", "").replace(",", ".")
        desc = response.css(
            "div.product.attribute.description div::text").get()
        other_desc = response.css(
            "div.product.attribute.short_description li::text").getall()
        for other in other_desc:
            desc += "\n - " + other
        images = response.css(
            "li.product-image-mosaic__grid__item img::attr(data-original)").getall()
        product = {
            "name": name,
            "ref": ref,
            "desc": desc,
            "images": images,
            "price": float(price),
            "reducedPrice": float(reducedPrice),
            "url": response.url,
            "brand": "Eastpak",
            "currency": "EUR",
            "from": self.process_id,
            "meta": {"category": response.meta["category"]}
        }
        self.products.append(product)
