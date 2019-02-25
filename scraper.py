import scrapy


class CapitaldePremiosSpider(scrapy.Spider):
    name = "capital_de_premios_spider"
    start_urls = ["http://www.capitaldepremios.com.br/resultados-atualizado/"]

    def parse(self, response):
        v = {
            "title": response.xpath('//h3/text()').extract(),
            "numeros": response.xpath('//div[@class="numeros"]/ul/li/text()').extract()
        }
    
        prim = 0  # int(input("1: "))
        prim1 = 38  # int(input("1.5: "))
        seg = 38  # int(input("2: "))
        seg1 = 74  # int(input("2.5: "))
        ter = 74  # int(input("3: "))
        ter1 = 113  # int(input("3.5: "))
        quar = 113  # int(input("4: "))
        quar1 = 149  # int(input("4.5: "))

        #p1t = v["title"][0]
        p1 = v["numeros"][prim:prim1]
        lista_p1 = [p1]

        #p2t = v["title"][2]
        p2 = v["numeros"][seg:seg1]
        lista_p2 = [p2]

        #p3t = v["title"][3]
        p3 = v["numeros"][ter:ter1]
        lista_p3 = [p3]

        #p4t = v["title"][4]
        p4 = v["numeros"][quar:quar1]
        lista_p4 = [p4]

        #print("1° Premio: {}\n2° Premio: {}\n3° Premio: {}\n4° Premio: {}\n".format(lista_p1, lista_p2, lista_p3, lista_p4))
        
        l = ['05', '06', '08', '10', '13', '14', '15', '16', '26', '27', '28', '31', '32', '36', '37', '39', '43', '52', '59', '60']
        """
        c = 0
        while c < 20:
            print()

            num = input("Digite os numeros da cartela: (example: 01, 02, 03, ...): ")
            l.append(num)
            c += 1
        
        print()        
        """

        #Sorteio 1
        i = 0
        while i < len(l):
            if (l[i] in lista_p1[0]) == False:
                n = l[i]
                l.remove(n)
            i +=1
            if i >= len(l) : print("1: {}".format(l))
        
        
        #Sorteio 2 
        i = 0
        while i < len(l):
            if (l[i] in lista_p2[0]) == False:
                n = l[i]
                l.remove(n)
            i +=1
            if i >= len(l): print("2: {}".format(l))
        
        #Sorteio 3 
        i = 0
        while i < len(l):
            if (l[i] in lista_p3[0]) == False:
                n = l[i]
                l.remove(n)
            i +=1
            if i >= len(l): print("3: {}".format(l))
                
        #Sorteio 4 
        i = 0
        while i < len(l):
            if (l[i] in lista_p4[0]) == False:
                n = l[i]
                l.remove(n)
            i +=1
            if i >= len(l): print("4: {}".format(l))
        
        return v

