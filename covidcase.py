## import packets

import scrapy
import re

## Create "no_accent_vietnamese" function using Regx to transform Vietnamese(UTF-8) to latin characters

def no_accent_vietnamese(s):
    s = re.sub(r'[àáạảãâầấậẩẫăằắặẳẵ]', 'a', s)
    s = re.sub(r'[ÀÁẠẢÃĂẰẮẶẲẴÂẦẤẬẨẪ]', 'A', s)
    s = re.sub(r'[èéẹẻẽêềếệểễ]', 'e', s)
    s = re.sub(r'[ÈÉẸẺẼÊỀẾỆỂỄ]', 'E', s)
    s = re.sub(r'[òóọỏõôồốộổỗơờớợởỡơ]', 'o', s)
    s = re.sub(r'[ÒÓỌỎÕÔỒỐỘỔỖƠỜỚỢỞỠƠ]', 'O', s)
    s = re.sub(r'[ìíịỉĩ]', 'i', s)
    s = re.sub(r'[ÌÍỊỈĨ]', 'I', s)
    s = re.sub(r'[ùúụủũưừứựửữư]', 'u', s)
    s = re.sub(r'[ƯỪỨỰỬỮÙÚỤỦŨ]', 'U', s)
    s = re.sub(r'[ỳýỵỷỹ]', 'y', s)
    s = re.sub(r'[ỲÝỴỶỸ]', 'Y', s)
    s = re.sub(r'[Đ]', 'D', s)
    s = re.sub(r'[đ]', 'd', s)

    marks_list = [u'\u0300', u'\u0301', u'\u0302', u'\u0303', u'\u0306',u'\u0309', u'\u0323']

    for mark in marks_list:
        s = s.replace(mark, '')

    return s

## Define spider name "covidcase" to crawl data and import to JSON file

class CovidcaseSpider(scrapy.Spider):
    name = "covidcase"
    allowed_domains = ["web.archive.org"]

    ## Define start_request which changed the request's header arguments
    def start_requests(self):
        yield scrapy.Request(url='https://web.archive.org/web/20210907023426/https://ncov.moh.gov.vn/vi/web/guest/dong-thoi-gian', callback=self.parse, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
        })

    ## Process response after request
    def parse(self, response):

        ## Get only the needed data (each datum contain attributes) - using xpath to identifiy
        allday = response.xpath("//div[@class='timeline-detail']")
        
        ## Extract and transform attriburtes from datum
        for day in allday:

            ## Extract attributes
            time = day.xpath(".//div[1]/h3/text()").get()
            new_case = no_accent_vietnamese(day.xpath(".//div[2]/p[2]/text()").get())
            cities = no_accent_vietnamese(day.xpath(".//div[2]/p[3]/text()").get())
            cities_detail = re.findall("\s[A-Z].*?\)",cities)

            ## Transform to dictionaries, required format
            city_case = []
            for city in cities_detail:
                each_day = {}
                each_day["city"] = re.findall('([A-Z].*?)\s\(',city)
                each_day["case"] = re.findall('\((\d+)\)',city)
                city_case.append(each_day)
            
            yield {
                "time": time,
                "new_case": re.findall("\s(\d.*?)\s",new_case)[0],
                "city_case": city_case
            }
        
        ## Get next_page link from "tiep theo" button after finish the current page
        next_page = response.xpath("//ul[@class='lfr-pagination-buttons pager']//li[2]/a/@href").get()

        ## If has next_page, then change the url and request again
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
            })
