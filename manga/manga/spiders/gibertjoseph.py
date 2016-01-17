# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from manga.items import MangaItem


class GibertjosephSpider(CrawlSpider):
    name = 'gibertjoseph'
    allowed_domains = ['gibertjoseph.com']
    start_urls = ['http://www.gibertjoseph.com/livres/bd/mangas-1.html?facet_status=Neuf&order=desc_release']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagination li a'))),
        Rule(LinkExtractor(allow=(), restrict_css=('.item_blocs_produit a')), callback='parse_item'),
    )

    def parse_item(self, response):
        # self.logger.info('Hi, this is an item page! %s', response.url)
        item = MangaItem()
        item['name'] = response.xpath('//h1[@class="product_title"]/a/text()').extract()
        item['description'] = response.xpath('//ul[@class="description"]/li[@class="truncated"]/div/text()').extract()
        item['release_date'] = response.xpath('//ul[@class="column"]/li/text()')[3].extract()
        item['author'] = response.xpath('//span[@class="author"]/a/text()').extract()
        item['editor'] = response.xpath('//ul[@class="column"]/li/text()')[2].extract()
        item['cover'] = response.xpath('//div[@class="defil_visuel"]/div[@class="visuel"]/span/a[@class="fancybox"]/img/@src').extract()
        # item['isbn'] = response.xpath('//div[@class="content"]/ul/li/text()')[1].extract()
        # item['collection'] = response.xpath('//div[@class="content"]/ul/li/text()')[5].extract()
        # item['pages'] = response.xpath('//div[@class="content"]/ul/li/text()')[6].extract()
        return item
