# -*- coding: UTF-8 -*-
# Autor: Ramon Serrano
# Correo <ramon_calle-88@hotmail.com>
#***********************************************************
# 2 Niveles de encriptacion :                            ***
## -- 0x  					                             ***
## -- 2 caracteres por caracter(letra, numero, caracter) ***
#***********************************************************
class SREncripter:
	global __LETRAS_MINUSCULAS, __LETRAS_MIN_ENC, __LETRAS_MAYUSCULAS, __LETRAS_MAY_ENC, __NUMEROS, __NUMEROS_ENC, __CARACTERES, __CARACTERES_ENC
	__LETRAS_MINUSCULAS = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
	__LETRAS_MIN_ENC = ['!n','(y','#)','()','{}','[]','{]','{)','(}','[}','[)','(]','*!','!*','?#','!@','n#','+$','=|','$#','~!','!~','||','[*','&}','@#',')_']
	__LETRAS_MAYUSCULAS = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','Ñ','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	__LETRAS_MAY_ENC = [':;',';:','.,',',.','/?','?/','?!','!?','$%','/#','?&','-_','=-','+-','<>','/>','w^','..',',&','@=','|`','`+','`)','`{','\}','""','+{']
	__NUMEROS = ['1','2','3','4','5','6','7','8','9','0']
	__NUMEROS_ENC = ['az','by','cx','dw','ev','fu','gt','hs','ir','jq','kp']
	__CARACTERES = ['\t','\n',' ','\\','`','~','!','@','#','$','%','^','&','*','(',')','_','+','=','-','|',"'",'"',';',':','/','?','.',',']
	__CARACTERES_ENC = ['aH','zA','aB','bC','cD','dE','eF','fG','gH','hI','iJ','jK','kL','lM','mN','nO','NO','oP','pQ','qR','rS','sT','tU','uV','vW','wX','xY','Ox']
	def __init__(self):
		#print self.letras_min, self.letras_may
		print "SREncripter Version 0.1"
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
			if i == ' ':
				self.aux += '0x0'
		return self.aux
	#*******Funcion para encriptar una palabra de nivel 2*********
	def __SRE_encripter2( self, palabra ):
		self.aux = ''
		for i in palabra:
			self.contador = 0
			for j in __NUMEROS:
				if i == j:
					#print self.contador
					self.aux += __NUMEROS_ENC[self.contador]
				self.contador += 1
			self.contador = 0
			for j in __LETRAS_MINUSCULAS:
				if i == j:
					#print self.contador
					self.aux += __LETRAS_MIN_ENC[self.contador]
				self.contador += 1
			self.contador = 0
			for j in __LETRAS_MAYUSCULAS:
				if i == j:
					#print self.contador
					self.aux += __LETRAS_MAY_ENC[self.contador]
				self.contador += 1
			self.contador = 0
			for j in __CARACTERES:
				if i == j:
					#print self.contador
					self.aux += __CARACTERES_ENC[self.contador]
				self.contador += 1
		return self.aux
	#Funcion de encriptar por metodos
	##Aun en ingenieria...
	def SRE_encripter(self, metodo, palabra):
		self.palabra = palabra
		if metodo == 1:
			return self.__SRE_encripter(self.palabra)
		if metodo == 2:
			return self.__SRE_encripter2(self.palabra)
	#Funcion de encriptar por metodos
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
			#self.plb_completa += i
		return self.plb_cmplt
	#*******Funcion para encriptar una palabra de nivel 2*********
	def __SRE_desencripter2( self, palabra ):
		self.plb_cmplt = ''
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
		if letra == '0x0':
			self.aux = ' '
		#letras minusculas
		elif letra == '0xa':
			self.aux = 'a'
		elif letra == '0xb':
			self.aux = 'b'
		elif letra == '0xc':
			self.aux = 'c'
		elif letra == '0xd':
			self.aux = 'd'
		elif letra == '0xe':
			self.aux = 'e'
		elif letra == '0xf':
			self.aux = 'f'
		elif letra == '0xg':
			self.aux = 'g'
		elif letra == '0xh':
			self.aux = 'h'
		elif letra == '0xi':
			self.aux = 'i'
		elif letra == '0xj':
			self.aux = 'j'
		elif letra == '0xk':
			self.aux = 'k'
		elif letra == '0xl':
			self.aux = 'l'
		elif letra == '0xm':
			self.aux = 'm'
		elif letra == '0xn':
			self.aux = 'n'
		elif letra == '0xñ':
			self.aux = 'ñ'
		elif letra == '0xo':
			self.aux = 'o'
		elif letra == '0xp':
			self.aux = 'p'
		elif letra == '0xq':
			self.aux = 'q'
		elif letra == '0xr':
			self.aux = 'r'
		elif letra == '0xs':
			self.aux = 's'
		elif letra == '0xt':
			self.aux = 't'
		elif letra == '0xu':
			self.aux = 'u'
		elif letra == '0xv':
			self.aux = 'v'
		elif letra == '0xw':
			self.aux = 'w'
		elif letra == '0xx':
			self.aux = 'x'
		elif letra == '0xy':
			self.aux = 'y'
		elif letra == '0xz':
			self.aux = 'z'
		#letras mayusculas	
		elif letra == '0xA':
			self.aux = 'A'
		elif letra == '0xB':
			self.aux = 'B'
		elif letra == '0xC':
			self.aux = 'C'
		elif letra == '0xD':
			self.aux = 'D'
		elif letra == '0xE':
			self.aux = 'E'
		elif letra == '0xF':
			self.aux = 'F'
		elif letra == '0xG':
			self.aux = 'G'
		elif letra == '0xH':
			self.aux = 'H'
		elif letra == '0xI':
			self.aux = 'I'
		elif letra == '0xJ':
			self.aux = 'J'
		elif letra == '0xK':
			self.aux = 'K'
		elif letra == '0xL':
			self.aux = 'L'
		elif letra == '0xM':
			self.aux = 'M'
		elif letra == '0xN':
			self.aux = 'N'
		elif letra == '0xÑ':
			self.aux = 'Ñ'
		elif letra == '0xO':
			self.aux = 'O'
		elif letra == '0xP':
			self.aux = 'P'
		elif letra == '0xQ':
			self.aux = 'Q'
		elif letra == '0xR':
			self.aux = 'R'
		elif letra == '0xS':
			self.aux = 'S'
		elif letra == '0xT':
			self.aux = 'T'
		elif letra == '0xU':
			self.aux = 'U'
		elif letra == '0xV':
			self.aux = 'V'
		elif letra == '0xW':
			self.aux = 'W'
		elif letra == '0xX':
			self.aux = 'X'
		elif letra == '0xY':
			self.aux = 'Y'
		elif letra == '0xZ':
			self.aux = 'Z'
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
