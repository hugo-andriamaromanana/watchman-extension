import scrapy
import chompjs
from lib.Base_Class import Base_Class


class Sevres24(Base_Class):
    def __init__(self):
        super().__init__()

    name = "24sevres"
    process_id = "63f8d06d2230586c01278a9a"

    custom_settings = {
        'DOWNLOAD_DELAY': 6,
        'RANDOMIZE_DOWNLOAD_DELAY': True,
    }

    start_urls = [
        "https://www.24s.com/fr-fr/femme/pret-a-porter?page=1",
        "https://www.24s.com/fr-fr/femme/chaussures?page=1",
        "https://www.24s.com/fr-fr/femme/sacs?page=1",
        "https://www.24s.com/fr-fr/femme/accessoires?page=1",
        "https://www.24s.com/fr-fr/femme/bijoux?page=1",
        "https://www.24s.com/fr-fr/homme/pret-a-porter?page=1",
        "https://www.24s.com/fr-fr/homme/chaussures?page=1",
        "https://www.24s.com/fr-fr/homme/chaussures/sneakers?page=1",
        "https://www.24s.com/fr-fr/homme/sacs?page=1",
        "https://www.24s.com/fr-fr/homme/accessoires?page=1",
    ]

    def parse(self, response, **kwargs):
        scripts = response.css(
            "script[type='application/ld+json']::text").getall()
        scripts = [chompjs.parse_js_object(script) for script in scripts]
        scripts = [script for script in scripts if script.get(
            "@type") == "Product"]
        for script in scripts:
            yield scrapy.Request(script.get("url"), callback=self.parse_product)
        if len(scripts) > 0:
            current_page = int(response.url.split("page=")[1])
            yield scrapy.Request(response.url.split("page=")[0] + "page=" + str(current_page + 1), callback=self.parse)

    def parse_product(self, response):
        parsed = chompjs.parse_js_object(
            response.css("script#__NEXT_DATA__::text").get())
        ldJson = [chompjs.parse_js_object(script) for script in response.css(
            "script[type='application/ld+json']::text").getall()]
        productJson = [script for script in ldJson if script.get(
            "@type") == "Product"][0]
        productRaw = parsed.get("props").get(
            "initialState").get("pdp").get("productFormated")
        name = productRaw.get("name")
        brand = productRaw.get("brand").get("name")
        ref = productRaw.get("longSKU")
        desc = ", ".join(productRaw.get("bulletPoints"))
        images = [productJson.get("image")]
        offerId = productRaw.get("offerId")
        prices = parsed["props"]["initialState"]["currency"]["convertedPrices"]
        prices = [price for price in prices if price.get("id") == offerId]
        price = [price for price in prices if price.get(
            "type") == "notDiscountedPrice"]
        price = price[0].get("prices").get("EUR")
        reducedPrice = [price for price in prices if price.get(
            "type") == "discountedPrice"]
        reducedPrice = reducedPrice[0].get("prices").get(
            "EUR") if len(reducedPrice) > 0 else price
        composition = productRaw.get("productInformation").get("composition")
        color = productRaw.get("productInformation").get("facetColor")
        category = " | ".join([cat.get("label")
                              for cat in productRaw.get("hierarchicalCategories")])
        prInf = productRaw.get("productInformation")
        meta = {
            "year": prInf.get("year"),
            "season": prInf.get("season"),
            "madeIn": prInf.get("madeIn"),
            "brandColor": prInf.get("brandColor"),
        }
        product = {
            "name": name,
            "ref": ref,
            "desc": desc,
            "brand": brand,
            "images": images,
            "price": float(price)/100,
            "reducedPrice": float(reducedPrice)/100,
            "url": response.url,
            "composition": composition,
            "color": color,
            "category": category,
            "meta": meta,
            "from": self.process_id,
            "currency": "EUR",
        }

        self.products.append(product)
