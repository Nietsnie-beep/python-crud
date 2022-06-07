clients = 'Nietsnie, Alberto' #creamos el string

def _print_welcome(): #funcion para dar el mensaje de bienvenida
	print ('Welcome to Monares POS')
	print ('what would you like to do today?')
	print ('*' * 52)  #imprimimos el caracter "*" 52 veces
	print ('[C]reate client')
	print ('[D]elete client')

def create_client(client_name):
	global clients  #Utilizamos global para definir que la variable es la globarl, es decir la que definimos con pablo y ricardo
 
	clients_minusculas = clients.lower() #convertimos la cadena de texto en minusculas y la guardamos en otra variable para no diferenciar entre "Pablo" y "Pablo"
 
	if client_name not in clients_minusculas: #si el nombre del cliente no esta en clients_minusculas
		_add_coma() #ejecutamos la funcion _add_coma para agregar una coma y un espacio 
		clients += client_name  #adicionamos el nuevo string
	else:
		print('Client already exists') #Sino mostramos un mensaje al usuario
def _add_coma():  #el nombre de la función comienza con un guión bajo para establecer que será una funcion privada
	global clients
	clients +=", " #se agrega una coma y un espacio al string para separar los nuevos valores


def list_clients(): #función que muestra la lista de clientes
	global clients
	print (clients) #imprimimos el string clientes


if __name__ == '__main__': #funcion main
	_print_welcome() #ejecutamos la funcion que da el mensaje de bienvenida
	command = input().lower() #guardamos el valor del dato ingresado en la variable command pero lo convertimos a miunsculas para realizar la accion si presiona "C" o "c"
	if command == 'c': #si el comando es igual al caracter "c"
		client_name = input('What is the client name?')  #guardamos en la variable client_name el valor de los caracteres que ingresa el usuario hasta recibir un enter
		create_client(client_name) #ejecutamos la funcion crear cliente y enviamos como parametro el valor de la variable que almacena lo que digitó el usuario
		list_clients() #Ejecutamos la funcion listar clientes 
	elif command == 'd': #si el dato ignresado por el usuario es "d"
		pass
	else:
		print('Invalid command')
input() #Escribimos un input para que el programa haga una pausa y no cierre la ventana hasta recibir un enter