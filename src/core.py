import sys
from scrapy.crawler import CrawlerProcess
from lib.thebradery import TheBradery
from lib.bazarchic import Bazarchic
from lib.lacoste import Lacoste
from lib.kikikickz import Kikikickz
from lib.steve_madden_india import Steve_madden_india
from lib.eastpak_fr import Eastpak_fr
from lib.thenorthface_fr import Thenorthface_Fr
from lib.alaia_fr import Alaia_fr
from lib.sketchers_fr import Sketchers_fr
from lib.havaianas_fr import Havaianas_fr
from lib.sevres24 import Sevres24
from lib.dickies import Dickies_fr

spiderTable = {
    "63821ac7b3353ff3a8cc7ce5": TheBradery,
    "63852c7e3ce5b10a25d911d7": Bazarchic,
    "638e1dd7bb49205cbe876772": Lacoste,
    "63be8fc4bc73f6d57c55bb52": Kikikickz,
    "63d7f19ecea0ba7f1e5b726c": Steve_madden_india,
    "63e25cdd1b81cce088d6a998": Eastpak_fr,
    "63eb88433774de0fc30841bf": Thenorthface_Fr,
    "63ef3b2c4b17ace89f42ed8b": Alaia_fr,
    "63f38f1ae8021ab1d4304c35": Sketchers_fr,
    "63f619776ecb79dbb7ab2794": Havaianas_fr,
    "63f8d06d2230586c01278a9a": Sevres24,
    "64060b2f009ba64eacde7c79": Dickies_fr,
}

process = CrawlerProcess()
process.crawl(spiderTable[sys.argv[1]])
process.start()