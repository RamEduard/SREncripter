# Se puede encriptar archivos de extension .txt, .py, u otros que 
# no contengan los caracteres < y >
#Importo la clase
from srencripter import *
#Hago una instancia de la clase
obj = SREncripter()
#Hago una instancia a un archivo de lectura
f = file('archivos/prueba.txt','r')
#Leo el archivo y guardo el contenido en una variable para trabajar con Este
p = f.read()
#Escribo p para ver el contenido del archivo
print p
#Encriptar o decriptar contenido de archivo por el metodo 2 que es para archivos
#PE = obj.SRE_encripter(2,p)
#PE = obj.SRE_desencripter(2,p)
print PE
f.close()
#Para reemplazar el archivo con el contenido encriptado o decriptado
#f = file('archivos/prueba.txt','w')
#f.write(PE)
#f.close()
