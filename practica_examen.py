#1 contar la cantidad de letras en una palabra ingresada por un usuario 
palabra = input("ingresa una palabra")
count = 0 

for letra in palabra: 
    count +=1
    print(count)


#2 Haz un programa que te calcule el promedio de una lista de calificaciones 
mis_claificaciones = [5, 8, 7, 10, 9] 
total = 0
for numero in mis_claificaciones:
    total += numero
calif = total/ len(mis_claificaciones)
print(calif)


#3 Haz un programa que te diga cual es el elemento mas grande de una lista 
lista = [32, 7, 19, 54, 28]
num_mayor = 0 
for mayor in lista:
    if mayor > num_mayor:
        num_mayor = mayor
print("el numero mayor de la lista es: ", num_mayor)

 
#4 Haz un programa que te indique cual es la palabra mas larga de una lista de palabras 
lista = ["cola", "vaca", "siempre", "parangaricutin"]
palabra_mayor = 0
mayor = ""
for palabra in lista:
    if palabra_mayor < len(palabra):
        mayor = palabra
        palabra_mayor = len(mayor)
print("palabra mayor de la lista es ", mayor)


#Haz un programa que te ayude a hacer una suma a partir de dos numeros ingresados por un usuario

# Haz un programa donde hagas una resta y te diga si el resultado es un numero positivo o negativo 

#Haz un programa donde a partir de 1 numero aleatorio del 1 al 10 y otro ingresado por el usuario, donde si son ihuales le diga que será acreedor a un cupon


#Haz un programa donde el usuario pueda solicitar ver una pelicula a partir de una lista dada por el sistema , dónde consideren su edad , 2 peliculas deben de ser para mayores de 18 años.

##Haz un programa que calcule el IMC, solicitandole al usuario tu altura y el peso. 

#Haz un programa que te ayude a calcular la calificación de un examen, donde el usuario deberá ingresar el total de preguntas, la cantidad de preguntas con respuestas correctas y la cantidad de preguntas con respuestas incorrectas.