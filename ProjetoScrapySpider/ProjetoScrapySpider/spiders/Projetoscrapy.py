import scrapy

class Projetoscrapy (scrapy.Spider):
    
    name = "coletor"

    def start_requests(self):

        urls = ["https://www.99freelas.com.br/projects?page=1"]

        for url in urls:
            yield scrapy.Request(url= url, callback= self.parse, meta= {"pagina": 1})

    def parse(self, response):
       
        for item in response.xpath("//li[contains (@class, 'result-item')]"):
                yield {

                "Titulo":  item.xpath("./hgroup/h1[@class='title']/a[@href]/text()").get(),
                "Descrição": item.xpath("./div[@class='item-text description formatted-text']/text()").getall(),
                "tags": item.xpath("./p[@class = 'item-text habilidades']").get()
                }

        try:
            
            pagina_atual = response.meta["pagina"] 
            proxima_pagina = pagina_atual + 1
            proxima_url = f"https://www.99freelas.com.br/projects?page={proxima_pagina}"

            yield scrapy.Request(url= proxima_url, callback= self.parse, meta= {"pagina": proxima_pagina})

        except:
             self.logger.info("Fim da Navegação")

                    
         
