import urllib.request,re

# this function is for find the value a href and to include one in list for one treatment
def findPages(texto):
    try:
        for f in re.finditer(r'<a href="/', texto): # value to be researched
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
        print(texto[ini:fim])
        
site = urllib.request.urlopen("") # target
texto = site.read().decode('utf8')
lista = []
findPages(texto)
findLink(lista)

           
    



