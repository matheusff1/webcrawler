import json                                                                                                                        # Define your item pipelines here
import pymongo
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class JsonPipeline:
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
        line = json.dumps(dict(item), ensure_ascii=False, indent=4) + ",\n"
        self.file.write(line)
        return item


class MongoPipeline:
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get("MONGO_URI"),
            mongo_db="RankingTheBrands",
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        try:
            self.db["Brands"].insert_one(ItemAdapter(item).asdict())
        except Exception as e:
            spider.logger.error(f"Erro ao inserir item: {e}")
        return item
