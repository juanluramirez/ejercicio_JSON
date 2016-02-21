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

