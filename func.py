import urllib.request,re
class Func:
    def __init__(self,site,metodo,texto):
        self.site = site
        self.metodo = metodo
        self.listaPosicao = []
        self.listaNome = []
        self.texto = texto
        
    def __str__(self):
        return('{0}'.format(self.listaNome))
    
    def conectSite(self):
        try:
            print("Conectando")
            self.site = urllib.request.urlopen(self.site)
            return self.decodeSite()
        except:return False
        
    def decodeSite(self):
        self.texto = self.site.read().decode(self.metodo)
        return self.findPosicao()

    
    def findPosicao(self):
        try:
            for f in re.finditer('<a href="/',self.texto):
                localizacao = (f.start(),f.end())
                self.listaPosicao.append(localizacao)
            return self.findLink()
        except:return False
                
    def findLink(self):
        for i in range(0,len(self.listaPosicao),1):
            ini = self.listaPosicao[i][0] + 10
            localizacaoAspa = self.texto.find('"', ini)
            fim = localizacaoAspa
            self.listaNome.append((self.texto[ini:fim]))
