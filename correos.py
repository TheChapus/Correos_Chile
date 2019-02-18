

#Codigo para obtener informacion de envios ---> CorreosChile
#Agradecimientos a @jsavargas

# Importamos las librerias
from bs4 import BeautifulSoup
import requests
import urllib
import httplib
import json
#RH352992401CN
#ALS00359081
# Pagina

ID = "CN750400915LT"#Aqui numero de seguimiento

link       = "http://seguimientoweb.correos.cl/ConEnvCorreos.aspx"
host       = "seguimientoweb.correos.cl"
parametros = urllib.urlencode({"obj_key":"Cor398-cc","obj_env":ID})
headers    = {
"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:49.0) Gecko/20100101 Firefox/49.0",
"Content-type": "application/x-www-form-urlencoded",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Referer": "http://www.correos.cl/SitePages/seguimiento/seguimiento.aspx?",
"Cookie":"__utma=30439597.1199029372.1476733240.1476733240.1477418931.2; __utmz=30439597.1476733240.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=30439597.2.10.1477418931; __utmc=30439597; __utmt=1"
}

conexion   = httplib.HTTPConnection(host)
conexion.request("POST", link, parametros, headers)
respuesta  = conexion.getresponse()
ver_source = respuesta.read()
data = []


if respuesta.status == 200:
	soup = BeautifulSoup(ver_source, 'html5lib')
	entradas = soup.find_all('tr')
	print "Tracking ID  : ",entradas[0].find_all('td')[1].text
	print "Entregado a  : ",entradas[0].find_all('td')[3].text
	print "Fecha        : ",entradas[1].find_all('td')[1].text
	print "Rut          : ",entradas[1].find_all('td')[3].text
	print "\n\n"

	for i in xrange(2,len(entradas)):
		columnas = entradas[i].find_all('td')
		if len(columnas)>0:
		   print "Fecha: ",columnas[1].text.strip(" ").replace("&nbsp", "").strip()
		   print "Estado: ",columnas[0].text.strip(" ").replace("&nbsp", "").strip()
		   print "Oficina: ",columnas[2].text.strip(" ").replace("&nbsp", "").strip()
		   #print "Fecha: %s Estado: %s Oficina: %s" % (columnas[1].text.strip(" ").replace("&nbsp", "").strip(),columnas[0].text.strip(" ").replace("&nbsp", "").strip(),columnas[2].text.strip(" ").replace("&nbsp", "").strip())
		   print "\n"
