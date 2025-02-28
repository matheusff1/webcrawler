import json                                                                                                                        # Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ScrapperPipeline:
    def open_spider(self, spider):
        if(spider.name == 'RankingTheBrands'):
            self.file = open("outputs/allbrands.json", "w", encoding="utf-8")
        elif(spider.name == 'PucCampinas'):
            self.file = open("outputs/allcourses.json", "w", encoding="utf-8")
        self.file.write("[")

    def close_spider(self, spider):
        self.file.write("]")
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(item, ensure_ascii=False, indent=4) + ",\n"
        self.file.write(line)
        return item
