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