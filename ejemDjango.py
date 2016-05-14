"""
name = "Pau"

#Funciones!! (esta es la funcion "hi")
def hi(name):
	if name == 'Ola':
		print('Hi Ola!')
	elif name == 'Pau':
		print('Hi Pau!')
	else:
		print('Hi anonymous!')
hi(name) #con esto mandas llamar la funcion anterior

#si ponemos un parametro en la funcion tenemos que ponerlo 
#tmb cuando lo mandamos llamar

"""

"""
def hi(name):
	print('Hi ' + name + '!')
hi("Rachel")
"""


colores = ['Blanco', 'Negro', 'Azul', 'Rojo', 'Cafe']

def color(name):
	print("color " +name+ "!!")

#Bucle p/imprimir el array anterior
for name in colores: #for variableTemporal in nombreArray
	color(name) #nombreFuncion()
	print("Next color")


#este for imprime un rango determinado de nums
max = 5
for actual in range(1,max):
	print(actual)