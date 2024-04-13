# Aritméticos: son todos aquellos que nos permiten hacer cualquier operación básica: suma, resta, multiplicación, división, modulos y potencias

suma = 2 + 4

multiplicacion = 3 * 3

resta = 2 - 2

division = 9/3 

# Lógicos: son aquellos que nos ayudan a operar con los datos booleanos. Usan los operadores and, or y not.

a = True 
b = False 

# Comparadores: nos sirven para comparar 2 tipos de datos, si son iguales, diferentes, mayor a, menor a, etc. 

x = 3
y = 3 

# Concatenación: el rpoceso de anexar una cadena al final de otra cadena. 

hola = "Hola"
hola_2 = "mundo"

concatenacion = hola + " " + hola_2


# Ejercicio 
monto_bruto = 50  
tasa_interes = 12
monto_interes = monto_bruto * tasa_interes / 100 
print (monto_interes)
tasa_bonificacion = 5
importe_bonificacion = monto_bruto * tasa_bonificacion / 100
print (importe_bonificacion)
monto_neto = (monto_bruto - importe_bonificacion) + monto_interes
print (monto_neto)
