from func import Func
site = 'http://www.google.com.br'
metodo = 'utf-8'
texto = None
site = Func(site,metodo,texto)

site.conectSite()
print(site)
