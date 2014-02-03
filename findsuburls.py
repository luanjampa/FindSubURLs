import urllib.request,re,sys

def decodeSite(site,metodo):
    texto = site.read().decode(metodo)
    return texto
# this function is for find the value a href and to include one in list for one treatment
def findPages(texto):
    try:
        for f in re.finditer(r'<a href="/', texto): # value to be researched
            localizacao = (f.start(),f.end())
            lista.append(localizacao)
            
        for f in re.finditer(r'<a href=\'/', texto): # value to be researched
            localizacao = (f.start(),f.end())
            lista.append(localizacao)
        
        
    except:
        print("Nenhum valor foi encontrado")
# here is the treatment for slice the link       
def findLink(lista):
    for i in range(0,len(lista),1):
        ini = lista[i][0] + 10
        localizacaoAspa = texto.find('"', ini)
        fim = localizacaoAspa
        lista2.append((texto[ini:fim]))
    for i in range(0,len(lista2),1):
        print(lista2[i])
    for i in range(0,len(lista2),1):
       print(url+'/'+lista2[i])
       
        

def conectSite(url):
     
    
    try:
        print('Conectando...', )
        site = urllib.request.urlopen(url)
        
        return site
    except:
        pass
        #print("Site invalido ou indisponivel")
        #return conectSite()
url = input(str('Exemplo: http://google.com.br \n Site: http://www.')) # targe  
site = conectSite(url)
metodo = 'utf-8' #input('exemplo: utf-8, latin-1, iso-8859-1 \n Metodo:')
texto = decodeSite(site,metodo)
lista = []
lista2 = []
findPages(texto)
tratado = findLink(lista)


