import sys #libreria para usar cosas del sistema de python

print(f"hola {sys.argv[1]}")
#realizar un script q imprima una palabra una cant de veces x parametro
if len (sys.argv) !=3: #por qué 3? porque 1 es el nombre y los otros dos son los dos parámetros, el num y la cadena  
    print("error, necesito 2 parametros")
else:
    for i in range(int(sys.argv[2])):
        print(sys.argv[1]) #argv 2 argv 1 [nombrescript, parametro 1(string), parametro 2 (num)]