import scrapy
import json
import chompjs
from scrapy.selector import Selector
import urllib
from lib.Base_Class import Base_Class

class Thenorthface_Fr(Base_Class):
    def __init__(self):
        super().__init__()

    name = "Thenorthface_Fr"
    process_id = "63eb88433774de0fc30841bf"

    base_url = "https://www.thenorthface.fr"

    start_urls = [
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fhomme-hauts&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fhomme-vestes%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_MEN%2FSC_FR_MEN-JACKETS&config_category=SC_FR_MEN-JACKETS&config_category_title=Manteaux%2C%20Parkas%2C%20Doudounes%20%26%20Vestes%20Homme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_MEN-JACKETS_FR&config_category_trigger=SC_MEN-JACKETS&config_categorytree_trigger=SC_MEN%2FSC_MEN-JACKETS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341156&config_unisexcategoryidentifier=MEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fhomme-pantalons-shorts&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fhomme-hauts%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_MEN%2FSC_FR_MEN-TOPS&config_category=SC_FR_MEN-TOPS&config_category_title=Hauts%20%26%20T-shirts%20Homme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_MEN-TOPS_FR&config_category_trigger=SC_MEN-TOPS&config_categorytree_trigger=SC_MEN%2FSC_MEN-TOPS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341157&config_unisexcategoryidentifier=MEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fchaussures-homme&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fhomme-pantalons-shorts%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_MEN%2FSC_FR_MEN-BOTTOMS&config_category=SC_FR_MEN-BOTTOMS&config_category_title=Pantalons%20%26%20Shorts%20%7C%20Homme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_MEN-BOTTOMS_FR&config_category_trigger=SC_MEN-BOTTOMS&config_categorytree_trigger=SC_MEN%2FSC_MEN-BOTTOMS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341158&config_unisexcategoryidentifier=MEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fhomme-accessoires&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fchaussures-homme%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_FOOTWEAR%2FSC_FR_FOOTWEAR-MEN&config_category=SC_FR_FOOTWEAR-MEN&config_category_title=Chaussures%20Homme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_FOOTWEAR-MEN_FR&config_category_trigger=SC_FOOTWEAR-MEN&config_categorytree_trigger=SC_FOOTWEAR%2FSC_FOOTWEAR-MEN&config_storeid=7006&config_split_category=true&config_mobile=false&config_categoryid=341191&config_unisexcategoryidentifier=FOOTWEAR&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-vestes&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fhomme-accessoires%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_MEN%2FSC_FR_MEN-ACCESSORIES&config_category=SC_FR_MEN-ACCESSORIES&config_category_title=ACCESSOIRES%20%7C%20HOMME%20%7C%20The%20North%20Face&config_collection=SC_FR_MEN-ACCESSORIES_FR&config_category_trigger=SC_MEN-ACCESSORIES&config_categorytree_trigger=SC_MEN%2FSC_MEN-ACCESSORIES&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341160&config_unisexcategoryidentifier=MEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",

        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-hauts&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-vestes%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_WOMEN%2FSC_FR_WOMEN-JACKETS&config_category=SC_FR_WOMEN-JACKETS&config_category_title=Parkas%2C%20Vestes%20%26%20Manteaux%20Femme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_WOMEN-JACKETS_FR&config_category_trigger=SC_WOMEN-JACKETS&config_categorytree_trigger=SC_WOMEN%2FSC_WOMEN-JACKETS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341165&config_unisexcategoryidentifier=WOMEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-pantalons&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-hauts%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_WOMEN%2FSC_FR_WOMEN-TOPS&config_category=SC_FR_WOMEN-TOPS&config_category_title=Vestes%2C%20Sweats%20%26%20T-Shirts%20Femme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_WOMEN-TOPS_FR&config_category_trigger=SC_WOMEN-TOPS&config_categorytree_trigger=SC_WOMEN%2FSC_WOMEN-TOPS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341166&config_unisexcategoryidentifier=WOMEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fchaussures-femme&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-pantalons%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_WOMEN%2FSC_FR_WOMEN-BOTTOMS&config_category=SC_FR_WOMEN-BOTTOMS&config_category_title=Pantalons%20%26%20Leggings%20de%20Sport%20Femme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_WOMEN-BOTTOMS_FR&config_category_trigger=SC_WOMEN-BOTTOMS&config_categorytree_trigger=SC_WOMEN%2FSC_WOMEN-BOTTOMS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341167&config_unisexcategoryidentifier=WOMEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023"
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-accessoires&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fchaussures-femme%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_FOOTWEAR%2FSC_FR_FOOTWEAR-WOMEN&config_category=SC_FR_FOOTWEAR-WOMEN&config_category_title=Chaussures%20Femme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_FOOTWEAR-WOMEN_FR&config_category_trigger=SC_FOOTWEAR-WOMEN&config_categorytree_trigger=SC_FOOTWEAR%2FSC_FOOTWEAR-WOMEN&config_storeid=7006&config_split_category=true&config_mobile=false&config_categoryid=341192&config_unisexcategoryidentifier=FOOTWEAR&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fenfant-garcons&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Ffemme-accessoires%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_WOMEN%2FSC_FR_WOMEN-ACCESSORIES&config_category=SC_FR_WOMEN-ACCESSORIES&config_category_title=Accessoires%20%7C%20Femme%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_WOMEN-ACCESSORIES_FR&config_category_trigger=SC_WOMEN-ACCESSORIES&config_categorytree_trigger=SC_WOMEN%2FSC_WOMEN-ACCESSORIES&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341169&config_unisexcategoryidentifier=WOMEN&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",

        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fenfant-filles&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fenfant-garcons%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_KIDS%2FSC_FR_KIDS-BOYS&config_category=SC_FR_KIDS-BOYS&config_category_title=V%C3%AAtements%20%26%20Chaussures%20Outdoor%20Gar%C3%A7ons%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_KIDS-BOYS_FR&config_category_trigger=SC_KIDS-BOYS&config_categorytree_trigger=SC_KIDS%2FSC_KIDS-BOYS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341174&config_unisexcategoryidentifier=BOYS&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fenfant-petits-bebes-0-7-ans&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fenfant-filles%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_KIDS%2FSC_FR_KIDS-GIRLS&config_category=SC_FR_KIDS-GIRLS&config_category_title=V%C3%AAtements%20%26%20Chaussures%20Outdoor%20Filles%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_KIDS-GIRLS_FR&config_category_trigger=SC_KIDS-GIRLS&config_categorytree_trigger=SC_KIDS%2FSC_KIDS-GIRLS&config_storeid=7006&config_split_category=false&config_mobile=false&config_categoryid=341175&config_unisexcategoryidentifier=GIRLS&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
        "https://fsm-vfc.attraqt.com/zones-js.aspx?version=19.4.13&siteId=1d217a03-66b2-483b-8404-d3aff4841058&UID=b248bdbd-0f0b-62c5-7cab-2eee6132ee4c&SID=5de12bbb-bf20-f870-5f5f-67619a1d80aa&referrer=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fenfant-filles&sitereferrer=&pageurl=https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2Fenfant-petits-bebes-0-7-ans%23esp_pg%3D1&zone0=category_FR&facetmode=data&mergehash=true&currency=EUR_FR&language=fr_FR&region=fr_FR&config_country=FR&config_languageid=-2&config_categorytree=SC_FR_KIDS%2FSC_FR_KIDS-INFANTS&config_category=SC_FR_KIDS-INFANTS&config_category_title=V%C3%AAtements%20Enfant%20%26%20B%C3%A9b%C3%A9%20%7C%200-7%20Ans%20%7C%20The%20North%20Face%20FR&config_collection=SC_FR_KIDS-INFANTS_FR&config_category_trigger=SC_KIDS-INFANTS&config_categorytree_trigger=SC_KIDS%2FSC_KIDS-INFANTS&config_storeid=7006&config_split_category=true&config_mobile=false&config_categoryid=341176&config_unisexcategoryidentifier=KIDS&config_showunpublish=false&config_catalogid=13504&config_fsm_sid=5de12bbb-bf20-f870-5f5f-67619a1d80aa&config_fsm_returnuser=1&config_fsm_currentvisit=17%2F02%2F2023&config_fsm_visitcount=10&config_fsm_lastvisit=15%2F02%2F2023",
    ]

    def start_requests(self):
        for url in self.start_urls:
            category = url.split("pageurl=")[1].split("&")[0].split("%23esp_pg%3D1")[
                0].replace('https%3A%2F%2Fwww.thenorthface.fr%2Fshop%2Ffr%2Ftnf-fr%2F', "")
            yield scrapy.Request(url=url, callback=self.parse, meta={"category": category})

    def parse(self, response):
        raw = response.body.decode('utf-8')
        raw = raw.replace('try {LM.buildStart();} catch (e) {};', '')
        parsed = chompjs.parse_js_object(raw)
        rawHtml = parsed['html']
        htmlSelector = Selector(text=rawHtml)
        productLinks = htmlSelector.xpath(
            '//a[@class="product-block-name-link"]')
        if productLinks != []:
            responseUrl = response.url
            urlparse = urllib.parse.urlsplit(responseUrl)
            query = dict(urllib.parse.parse_qsl(urlparse.query))
            pageUrl = query['pageurl']
            newPageUrl = pageUrl.split(
                "esp_pg=")[0] + "esp_pg=" + str(int(pageUrl.split("esp_pg=")[1])+1)
            query['pageurl'] = newPageUrl
            urlparse = urlparse._replace(query=urllib.parse.urlencode(query))
            newUrl = urllib.parse.urlunsplit(urlparse)
            yield scrapy.Request(url=newUrl, callback=self.parse, meta=response.meta)

        for product in productLinks:
            productUrl = product.xpath('@href').get()
            yield scrapy.Request(url="https://www.thenorthface.fr" + productUrl, callback=self.parseProduct, meta=response.meta)

    def parseProduct(self, response):
        variations = response.css(
            'img.color-swatch-button-content::attr(data-variation-id)').getall()
        for variation in variations:
            url = "https://www.thenorthface.fr/shop/fr/tnf-fr/" + \
                response.url.split("?")[0].split(
                    "/")[-1] + "?variationId=" + variation
            yield scrapy.Request(url=url, callback=self.parseProductVariation, meta=response.meta)
        yield scrapy.Request(url=response.url, callback=self.parseProductVariation, meta=response.meta)

    def parseProductVariation(self, response):
        name = response.css("meta[property='og:title']::attr(content)").get()
        desc = ""
        try:
            productDesc = response.css(
                "script:contains('pwr(\"render\"')::text").get()
            productDesc = productDesc.split("pwr(\"render\",")[1]
            parsedProductDesc = chompjs.parse_js_object(productDesc)
            desc = parsedProductDesc["product"]["description"]
        except:
            pass
        span_hide = response.css(
            "span.tracking-product-data-js::attr(data-tracking-product-data-service-options)").get()
        parsedSpan = chompjs.parse_js_object(span_hide)
        price = parsedSpan['price']
        variationId = response.url.split("variationId=")[1]
        data_product_data = response.css(
            "img[data-variation-id='"+variationId+"']::attr(data-product-data)").get()
        data_product_data = json.loads(data_product_data)
        meta = {
            "model": data_product_data['styleCode'],
            "color_code": response.url.split("variationId=")[1],
        }
        productIdSystem = response.css(
            "meta[property='og:productId']::attr(content)").get()
        pricingscript = response.css(
            "script:contains('var itemPrices')::text").get()
        parsedPrice = chompjs.parse_js_object(pricingscript)
        rrp = parsedPrice[productIdSystem]["pricing"]["default"]["highListPriceNumeric"]
        ref = data_product_data['styleCode']
        images = response.css(
            "div.mol-media-gallery__cell__overlay::attr(data-preview-image-uri)").getall()
        product = {
            "name": name,
            "ref": ref,
            "desc": desc,
            "images": images,
            "price": float(rrp),
            "reducedPrice": float(price),
            "url": response.url,
            "brand": "The North Face",
            "category": response.meta["category"],
            "color" : data_product_data['colorDescription'],
            "meta": meta,
            "from": self.process_id,
            "currency": "EUR",
        }
        self.products.append(product)
