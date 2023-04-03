import scrapy
import chompjs
from lib.Base_Class import Base_Class


class Dickies_fr(Base_Class):
    def __init__(self):
        super().__init__()
        
    name = "Dickies_fr"
    processId = "64060b2f009ba64eacde7c79"
    start_urls = ["https://www.dickieslife.com/fr_fr/homme?p=1",
                  "https://www.dickieslife.com/fr_fr/femme?p=1",
                  ]

    def parse(self, response):
        items = response.css("a.product-item-link::attr(href)").extract()
        for i in items:
            yield scrapy.Request(i, callback=self.parseProduct)
        if len(items) != 0:
            newUrl = response.url.split(
                "?p=")[0] + "?p=" + str(int(response.url.split("?p=")[1]) + 1)
            yield scrapy.Request(newUrl, callback=self.parse)

    def parseProduct(self, response):
        name = response.css(
            "span[data-ui-id='page-title-wrapper']::text").extract_first()
        ref = response.css(
            "form#product_addtocart_form::attr(data-product-sku)").extract_first()
        descPart1 = response.css(
            "div.product.attribute div.value p::text").get()
        part2 = response.css("div.details-feature-column li::text").extract()
        part2 = "\n - ".join(part2)
        desc = descPart1 + "\n" + part2
        images = response.css(
            "img.gallery-placeholder__image::attr(src)").extract()
        price = response.css("span.normal-price span.price::text").get()
        oldPrice = response.css("span.old-price span.price::text").get()
        if oldPrice is None:
            oldPrice = price
        price = float(price.replace("€", "").replace(",", "."))
        oldPrice = float(oldPrice.replace("€", "").replace(",", ".")) 
        categories = response.css("div.breadcrumbs a::text").getall()
        categories = categories[1:]
        categories = " > ".join(categories)
        script = response.css(
            "script:contains('colorpattern-wrapper-product-details')::text").get()
        parsed = chompjs.parse_js_object(script)
        color = parsed[".colorpattern-wrapper-product-details"]["colorpatternProductDetails"]["colorValue"]
        product_tab_item_desktop = response.css("div.product-tab-item-desktop")
        material = None
        for i in product_tab_item_desktop:
            if i.css("span::text").get() == "Matière":
                material = i.css("li::text").get()
                break
        if material is None:
            material = ""
        if "Homme" in categories:
            gender = "H"
        elif "Femme" in categories:
            gender = "F"
        else: 
            gender = ""
        product = {
            "name": name,
            "ref": ref,
            "desc": desc,
            "images": images,
            "price": price,
            "reducedPrice": oldPrice,
            "url": response.url,
            "brand": "Dickies",
            "from": self.processId,
            "currency": "EUR",
            "category": categories,
            "color": color,
            "gender": gender,
            "composition": material
        }
        self.products.append(product)
