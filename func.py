import urllib.request,re
class Func:
    def __init__(self,site,metodo,texto,cont):
        self.site = site
        self.cont = cont
        self.url = self.site
        self.metodo = metodo
        self.listaPosicao = []
        self.listaNome = []
        self.texto = texto
        
    def __str__(self):
        
        return ('{0}'.format(self.listaNome))
    
    def conectSite(self):
        try:
            self.site = urllib.request.urlopen(self.site)
            return self.decodeSite()
        except:return None
        
    def decodeSite(self):
        self.texto = self.site.read().decode(self.metodo)
        return self.findPosicao()

    
    def findPosicao(self):
        try:
            for f in re.finditer('<a href="',self.texto):
                localizacao = (f.start(),f.end())
                self.listaPosicao.append(localizacao)
            return self.findLink()
        except:return None
                
    def findLink(self):
        for i in range(0,len(self.listaPosicao),1):
            ini = self.listaPosicao[i][0] + 9
            fim = self.texto.find('"', ini)
            link = (self.texto[ini:fim])
            if link not in self.listaNome and (('www' not in link )and ('http://' not in link) and ('https://' not in link) and ('mailto' not in link)) : # poderia ser usado um for pegando os valores da lista aqui mais ficaria um pouco mais lento já que é um for dentro de outro
                #print(link)
                self.listaNome.append(link)
        del self.listaPosicao[:]
        return self.subURLS()
    
    def subURLS(self):
        print(self.cont)
        if self.cont <= len(self.listaNome):
            self.site = self.url + '/' + self.listaNome[self.cont]
            self.cont+=1
            return self.conectSite()
        else:
            print("Busca chegou ao fim")
        

    
