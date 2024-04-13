# Tuplas
# Listas / Arrays / Arreglos
# Diccionarios 

# Una tuplas es una variable que permite almacenar varios datos inmutables (no pueden ser modificados una vez creados)
# de tipos diferentes 
mi_tupla = (1, 'oscar', 90.5, 'méxico', 0.2)
print (mi_tupla[1])
# mi tupla [2] = 'a' No se puede modificar por que es una tupla, lanzará error. 
print (mi_tupla[2:5])


# Una lista es similar a una tupla con la diferencia fundamental de que permite modificar los datos una vez creados:
mi_lista = ['cadena de texto', 15, 2.8, 'Daniel', 30]
print(mi_lista[0])
mi_lista[0] = 'hola'
print(mi_lista)
mi_lista.append(999)
mi_lista.append(15)
mi_lista.remove(15)
mi_lista.pop(0)
print(mi_lista) 


# Los diccionarios permiten usar una clave para declarar y acceder a un valor 
mi_diccionario = {'x': '123'}
print (mi_diccionario['x'])

persona_0 = {'Nombre':'Juan', 'Nacionalidad': 'Alemana', 'Peso': '74'}
persona_1 = {'Nombre': 'Oscar', 'Nacionalidad': 'Mexicana', 'Peso': '69'}
print(persona_0['Peso'])
persona_0['peso'] = 78
print(persona_0)


dict = {
   'nombres' : ['Oscar', 'Daniel', 'Hernandez', 'Moreno'], 
   'Nacionalidad': 'Mexicana'
}

array = [
    {'Nombre': 'Juan', 'Nacionalidad': 'Mexicana', 'Peso': '74'}, 
    {'Nombre': 'Pedro', 'Nacionalidad': 'Peruana', 'Peso': '74'}, 
    {'Nombre': 'Miguel', 'Nacionalidad': 'Mexicana', 'Peso': '74'}, 
    {'Nombre': 'Kent', 'Nacionalidad': 'Americana', 'Peso': '74'},
]

array.pop(0)
print(array)
