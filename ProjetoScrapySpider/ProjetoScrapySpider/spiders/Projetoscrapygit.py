import scrapy

class Projetoscrapygit (scrapy.Spider):
    
    name = "XPTO"

    def start_requests(self):

        urls = ["insert the url here"]

        for url in urls:
            yield scrapy.Request(url= url, callback= self.parse, meta= {"pagina": 1})

    def parse(self, response):
       
        for item in response.xpath("insert the XPATH here"):
                yield {

                "XPTO":  item.xpath("./insert the XPATH here").get(),
                "XPTO": item.xpath("./insert the XPATH here").getall(),
                "XPTO": item.xpath("./insert the XPATH here").get()
                }

        try:
            
            pagina_atual = response.meta["pagina"] 
            proxima_pagina = pagina_atual + 1
            proxima_url = f"insert the url here{proxima_pagina}"

            yield scrapy.Request(url= proxima_url, callback= self.parse, meta= {"pagina": proxima_pagina})

        except:
             self.logger.info("XPTO")

                    
         
