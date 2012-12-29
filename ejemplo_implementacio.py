from srencripter import *
obj = SREncripter()
palabra = "Ramon Serrano \\~!@#$%^&*()_+`1234567890-[]|}{;:\"?/.,\t\n\tIdentacion"
#Utilizacion del metodo 1
print palabra
pppp = obj.SRE_encripter2(palabra)
print pppp
dd = obj.SRE_desencripter2(pppp)
print dd
#Utilizacion del metodo 2
print palabra
pppp2 = obj.SRE_encripter2(2,palabra)
print pppp2
dd2 = obj.SRE_desencripter2(2,pppp2)
print dd2
