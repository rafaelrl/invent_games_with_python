import random

def instrucciones():
	print("""Estoy pensando en un número de 3 dígitos. Intenta adivinar cuál es.
	Aquí hay algunas pistas:
	Cuando digo:
	Eso significa:
	Pico -- Un dígito es correcto pero en la posición incorrecta.

	Fermi -- Un dígito es correcto y en la posición correcta.

	Panecillos -- Ningún dígito es correcto.

	He pensado un número. Tienes 10 intentos para adivinarlo.""")
	
instrucciones()

numero = []
for i in range(3):
	numero.append(str(random.randint(1, 9)))
	

#print(numero)

intentos = 10


def numeroJugador(jugador):
	jugador2 = []
	for i in range(3):
		jugador2.append(jugador[i])
	return jugador2




while intentos >= 1:
	
	jugador = input('Escribe un número de 3 cifras: ')
	while len(jugador) != 3:
		jugador = input('Tu número es incorrecto. Por favor, escribe un número de TRES cifras: ')
	a = numeroJugador(jugador)
	
	resultado = [0, 0, 0]
	if a== numero:
		print('Has ganado')
		break
	for i in range(3):
		if a[i] == numero[i]:
			resultado[i] = 'Fermi'
			
		elif a[i] in numero:
			resultado[i] = 'Pico'
			
		else:
			resultado[i] = 'Panecillos'
	intentos -= 1
	print(resultado[0], resultado[1], resultado[2])
	print('Te quedan {} intento(s)'.format(intentos))
		
print('¡Has perdido!')		
