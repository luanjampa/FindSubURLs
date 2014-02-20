from func import Func
url = 'http://www.insoonia.com'
metodo = 'utf-8'
texto = None
cont = 0
site = Func(url,metodo,texto,cont)

site.conectSite()
print(site)
