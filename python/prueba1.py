def es_impar(numero):
    resto = numero % 2
    if resto == 0:
        print(' es par')
    else:
        print(' es impar')
lista = (1,3,5,4,6,8,2,10)
for numero in lista:
    es_impar(numero)

def es_impar_bool (numero):
    resto = numero % 2
    if resto == 0:
       return False
    else:
        return True

for numero in lista:
    print ('Procesamos numero ', numero)
    respuesta= es_impar_bool(numero)
    if respuesta:  # respuesta == True
        print('Es impar')
    else :
        print ('Es par')

  

def mayuscular(texto):
    return texto.upper()
def num_palabras(texto):
    return len(texto.split())


