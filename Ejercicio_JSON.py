# -*- coding: utf-8 -*-

import json
with open("comercios_comercios.json") as doc:
	doc=json.load(doc)

raiz=doc["resources"]

#1) Listar los negocios y su numero de telefono.

for comercios in raiz:
	print "El nombre del comercio es:",comercios["dc:name"],"y su telefono es",comercios["ayto:telefono"]

#2)Contar el numero de negocios que hay registrados en Santander.

print "Hay un total de",len(raiz),"comercios registrados."

#3)Introducir por teclado una cadena por la cual comienza la direccion por ejemplo: Al introducir calle, no aparecera el nombre del comercio y la calle donde se encuentra.

via=raw_input("Dime el inicio de la via: ")

for calles in raiz:
	if calles["ayto:direccion"].startswith(via.title()):
		print "El comercio es",calles["dc:name"],"y se encuentra en",calles["ayto:direccion"]

#4)Introducir el codigo o el idPuesto por teclado y nos mostrara el nombre del comercio y la calle.

id_comercio=raw_input("Dime el id del comercio o del puesto: ")

for codigos in raiz:
	if codigos["ayto:codigo"]==id_comercio:
		print "El comercio es",codigos["dc:name"],"y se encuentra en",codigos["ayto:direccion"]
	elif codigos["ayto:idPuesto"]==id_comercio:
		print "El puesto es",codigos["dc:name"],"y se encuentra en",codigos["ayto:direccion"]

#5)Obtendremos una lista de los negocios con su ubicacion en "openstreetmaps".

id_comercio=raw_input("Dime el id del comercio o del puesto: ")

for ubicacion in raiz:
	if ubicacion["ayto:codigo"]==id_comercio:
		latitud=ubicacion["ayto:latitud"]
		longitud=ubicacion["ayto:longitud"]
		print "El comercio es",ubicacion["dc:name"],"y su ubicacion en openstreetmap es:","http://www.openstreetmap.org/#map=25/"+latitud+"/"+longitud

#6)Genera un fichero html, con los datos de todos loc comercios que tienen pagina web, con la siguiente estructura:

for web in raiz:
	if web["ayto:web"]!="":
		fichero.write("<h1>"+web["dc:name"]+"</h1>"+"\n")
		fichero.write("<p>"+web["dc:description"]+"</p>"+"\n")
		fichero.write('a href="'+web["ayto:web"]+'">Más Informacion</a>')