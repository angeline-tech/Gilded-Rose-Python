class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                self.reduceQualityIfNotSulfuras(item)
            else:
                if item.quality < 50:
                    self.incrementItemQuality(item)
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            self.improveQualityIfLessThan50(item)
                        if item.sell_in < 6:
                            self.improveQualityIfLessThan50(item)

            self.reduceSellInIfNotSulfuras(item)

            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        self.reduceQualityIfNotSulfuras(item)
                    else:
                        self.setItemQualityToZero(item)
                else:
                    self.improveQualityIfLessThan50(item)

    def reduceSellInIfNotSulfuras(self, item):
        if item.name != "Sulfuras, Hand of Ragnaros":
            item.sell_in = item.sell_in - 1

    def incrementItemQuality(self, item):
        item.quality = item.quality + 1

    def setItemQualityToZero(self, item):
        item.quality = 0


    def improveQualityIfLessThan50(self, item):
        if item.quality < 50:
            self.incrementItemQuality(item)

    def reduceQualityIfNotSulfuras(self, item):
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = item.quality - 1
