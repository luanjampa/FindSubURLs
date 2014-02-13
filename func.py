import urllib.request,re
lista = [] #is used for save positions
lista2 = [] # is used after lista for slice the code
#values = [,"<a href='/"]
def decodeSite(site,metodo):
    texto = site.read().decode(metodo)
    return findPages(texto)
# this function is for find the value a href and to include one in list for one treatment
def findPages(texto):
    try:
        for f in re.finditer('<a href="/', texto):# value to be researched
            localizacao = (f.start(),f.end())
            lista.append(localizacao)
        return findLink(lista,texto)
    except:
        
        return False
# here is the treatment for slice the link       
def findLink(lista,texto):
    for i in range(0,len(lista),1):
        ini = lista[i][0] + 10
        localizacaoAspa = texto.find('"', ini)
        fim = localizacaoAspa
        lista2.append((texto[ini:fim]))
  #  for i in range(0,len(lista1),1):
  #      lista2.append((url+'/'+lista[i]))

        
def conectSite(url):
     
    try:
        print('Conectando...', )
        site = urllib.request.urlopen('http://www.' + url)
        return conectSite2(site)
    except:
       return False
    
def conectSite2(site):
    
    metodo = 'utf-8'#input('exemplo: utf-8, latin-1, iso-8859-1 \n Metodo:')
    texto = decodeSite(site,metodo)
    findLink(lista,texto)

def exibir():
    
   return lista2
