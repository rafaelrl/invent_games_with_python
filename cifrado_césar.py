
abecedario = list(chr(x) for x in range(ord(chr(32)), ord(chr(126))))
print(abecedario)
modo = input('¿Deseas encriptar o desencriptar un mensaje? ')

def encDesenc(modo):
	if modo == 'encriptar':
		return 'encriptar'
	elif modo == 'desencriptar':
		return 'desencriptar'
	else:
		print('Lo siento. No ha introducido una opción correcta. Saliendo del programa. . .')

def escribirMensaje(modo):
	mensaje = input('Escribe tu mensaje: ')
	if modo == 'encriptar':
		return mensaje.upper()
	elif modo == 'desencriptar':
		return mensaje

def desplazar():
	desplazamiento = int(input('Escribe el número de clave: '))
	return desplazamiento

a = escribirMensaje(modo)
b = desplazar()
encDesenc(modo)

def cifrar(a, b):
	if encDesenc(modo) == 'encriptar':
		encriptado = []
		for i in a:
			if i in abecedario:
				print(abecedario.index(i))
				nueva_posicion = int(abecedario.index(i)) + b
				#print('Nueva posición: ', type(nueva_posicion))
				encriptado.append(abecedario[nueva_posicion])
		return encriptado

def descifrar(a, b):
	if encDesenc(modo) == 'desencriptar':
		desencriptado = []
		for i in a:
			if i in abecedario:
				print(abecedario.index(i))
				nueva_posicion = int(abecedario.index(i)) - b
				print('Nueva posición', nueva_posicion)
				#print('Nueva posición: ', type(nueva_posicion))
				desencriptado.append(abecedario[nueva_posicion])
		return desencriptado

c = cifrar(a, b)

d = descifrar(a, b)

if c is not None:
	print(''.join(c))
elif d is not None:
	print(''.join(d))
	
