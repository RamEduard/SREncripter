# -*- coding: UTF-8 -*-
# Autor: Ramon Serrano
# Correo <ramon_calle-88@hotmail.com>
#***********************************************************
# 2 Niveles de encriptacion :                            ***
## -- 0x  					                             ***
## -- 2 caracteres por caracter(letra, numero, caracter) ***
#***********************************************************
import binascii
class SREncripter:
	global __LETRAS_MINUSCULAS, __LETRAS_MIN_ENC, __LETRAS_MAYUSCULAS, __LETRAS_MAY_ENC, __NUMEROS, __NUMEROS_ENC, __CARACTERES, __CARACTERES_ENC
	__LETRAS_MINUSCULAS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
	__LETRAS_MIN_ENC = ['!n','(y','#)','()','{}','[]','{]','{)','(}','[}','[)','(]','*!','!*','?#','!@','n#','+$','=|','$#','~!','!~','||','[*','&}','@#',')_']
	__LETRAS_MAYUSCULAS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	__LETRAS_MAY_ENC = [':;',';:','.,',',.','/?','?/','?!','!?','$%','/#','?&','-_','=-','+-','<>','/>','w^','..',',&','@=','|`','`+','`)','`{','\}','""','+{']
	__NUMEROS = ['1','2','3','4','5','6','7','8','9','0']
	__NUMEROS_ENC = ['az','by','cx','dw','ev','fu','gt','hs','ir','jq','kp']
	__CARACTERES = ['\t','\n',' ','\\','`','~','!','@','#','$','%','^','&','*','(',')','_','+','=','-','|',"'",'"',';',':','/','?','.',',','{','}','[',']']
	__CARACTERES_ENC = ['aH','zA','aB','bC','cD','dE','eF','fG','gH','hI','iJ','jK','kL','lM','mN','nO','NO','oP','pQ','qR','rS','sT','tU','uV','vW','wX','xY','Ox','YT','Ag','!M','WN','UX']
	def __init__(self):
		#print self.letras_min, self.letras_may
		print "SREncripter Version 0.6"
	#******************Funciones para Encriptar*******************
	#Funcion de encriptar palabra de nivel 1
	def __SRE_encripter( self, palabra ):
		self.aux = ''
		for i in palabra:
			for j in __LETRAS_MINUSCULAS:
				if i == j:
					self.aux += '0x'+i
			for j in __LETRAS_MAYUSCULAS:
				if i == j:
					self.aux += '0x'+i
			for j in __NUMEROS:
				if i == j:
					self.aux += '0x'+i
			for j in __CARACTERES:
				if i == j:
					self.aux += '0x'+i
		return self.aux
	#*******Funcion para encriptar una palabra de nivel 2*********
	def __SRE_encripter2( self, palabra ):
		self.aux = ''
		for i in palabra:
			self.contador = 0
			for j in __NUMEROS:
				if i == j:
					self.aux += __NUMEROS_ENC[self.contador]
				self.contador += 1
			self.contador = 0
			for j in __LETRAS_MINUSCULAS:
				if i == j:
					self.aux += __LETRAS_MIN_ENC[self.contador]
				self.contador += 1
			self.contador = 0
			for j in __LETRAS_MAYUSCULAS:
				if i == j:
					self.aux += __LETRAS_MAY_ENC[self.contador]
				self.contador += 1
			self.contador = 0
			for j in __CARACTERES:
				if i == j:
					self.aux += __CARACTERES_ENC[self.contador]
				self.contador += 1
		return binascii.b2a_base64(self.aux)
	#Funcion de encriptar por metodo
	##Aun en ingenieria...
	def SRE_encripter(self, metodo, palabra):
		if metodo == 1:
			return self.__SRE_encripter(palabra)
		elif metodo == 2:
			return self.__SRE_encripter2(palabra)
	#Funcion de desencriptar por metodo
	##Aun en ingenieria...
	def SRE_desencripter(self, metodo, palabra):
		self.palabra = palabra
		if metodo == 1:
			return self.__SRE_desencripter(self.palabra)
		if metodo == 2:
			return self.__SRE_desencripter2(self.palabra)
	#************Funciones para desencriptar***************************#
	#Funcion de desencriptar palabra que llama a la funcion de nivel 1
	def __SRE_desencripter(self,palabra):
		self.plb_cmplt = ''
		j = 0
		self.aux = ''
		for i in palabra:
			if j < 3:
				self.aux += i
				j = j + 1
				if j == 3:
					self.plb_cmplt += self.__dlevel1(self.aux)
			else:
				self.aux = ''
				self.aux += i
				j = 1
		return self.plb_cmplt
	#*******Funcion para encriptar una palabra de nivel 2*********
	def __SRE_desencripter2( self, palabra ):
		self.plb_cmplt = ''
		palabra = binascii.a2b_base64(palabra)
		j = 0
		self.aux = ''
		for i in palabra:
			if j < 2:
				self.aux += i
				j = j + 1
				if j == 2:
					self.plb_cmplt += self.__dlevel2(self.aux)
			else:
				self.aux = ''
				self.aux += i
				j = 1
		return self.plb_cmplt
	#Funcion de comparar para cambiar palabra encriptada por letras
	def __dlevel1(self, letra):
		self.aux = ''
		for i in __LETRAS_MINUSCULAS:
			if letra == ("0x"+i):
				self.aux = i
		for i in __LETRAS_MAYUSCULAS:
			if letra == ("0x"+i):
				self.aux = i
		for i in __NUMEROS:
			if letra == ("0x"+i):
				self.aux = i
		for i in __CARACTERES:
			if letra == ("0x"+i):
				self.aux = i
		return self.aux
	#Funcion de comparar para cambiar palabra encriptada por letras
	def __dlevel2(self, letra):
		self.contador = 0
		for i in __LETRAS_MAY_ENC:
			if i == letra:
				self.aux = __LETRAS_MAYUSCULAS[self.contador]
			self.contador += 1
		self.contador = 0	
		for i in __LETRAS_MIN_ENC:
			if i == letra:
				self.aux = __LETRAS_MINUSCULAS[self.contador]
			self.contador += 1
		self.contador = 0
		for i in __NUMEROS_ENC:
			if i == letra:
				self.aux = __NUMEROS[self.contador]
			else:
				self.contador += 1
		self.contador = 0
		for i in __CARACTERES_ENC:
			if i == letra:
				self.aux = __CARACTERES[self.contador]
			self.contador += 1
		return self.aux
#fin de la clase
