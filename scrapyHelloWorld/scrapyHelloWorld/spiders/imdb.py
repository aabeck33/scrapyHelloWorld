import scrapy


class ImdbSpider(scrapy.Spider):
    name = 'imdb'
    #allowed_domains = ['imdb.com']
    start_urls = ['https://www.imdb.com/chart/top']

    def parse(self, response):
        titulo = response.css('.titleColumn a::text').getall()
        ano = response.css('.secondaryInfo::text').getall()
        aval = response.css('strong::text').getall()
        for i in range(len(titulo)):
            yield{   # Nesse caso é melhor que o return.
                'id': i+1,
                'titulo': titulo[i],
                'ano': ano[i][1:-1],
                'aval': aval[i]
            }

'''
    def parse(self, response):
        for filmes in response.css('.titleColumn'):
            yield{   # Nesse caso é melhor que o return.
                'titulo': filmes.css('.titleColumn a::text').get(),
                'ano': filmes.css('.secondaryInfo::text').get()[1:-1],
                'aval': response.css('strong::text').get()
            }
'''