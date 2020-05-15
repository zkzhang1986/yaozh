# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class YaozhItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    # 产品名称
    productName = scrapy.Field()
    # 申请人中文名称
    chineseNameOfApplicant = scrapy.Field()
    # 申请人地址
    addressOfApplicant = scrapy.Field()
    # 保健功能
    healthCareFunction = scrapy.Field()
    # 功效成分/标志性成分含量
    contentOfFunctionalIngredients = scrapy.Field()
    # 主要原料
    mainRawMaterials = scrapy.Field()
    # 适宜人群
    suitablePopulation = scrapy.Field()
    # 不适宜人群
    unsuitablePeople = scrapy.Field()
    # 食用方法及食用量
    consumptionMethodAndQuantity = scrapy.Field()
    # 产品规格
    productSpecifications = scrapy.Field()
    # 保质期
    qualityGuaranteePeriod = scrapy.Field()
    # 贮藏方法
    storageMethod = scrapy.Field()
    # 注意事项
    mattersNeedingAttention = scrapy.Field()
    # 批准日期
    approvalDate = scrapy.Field()
    # 产品编号
    productNumber = scrapy.Field()
    # 批准文号
    approvalNo = scrapy.Field()
    # 有效期至
    validUntil = scrapy.Field()