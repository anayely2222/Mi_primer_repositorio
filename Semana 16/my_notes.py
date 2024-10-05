#Crear un archivo y escribir almenos tres lineas de notas personales,leer el archivo linea por linea y asegrarse al final de cerrar el archivo.
#Primero hacer la escritura del archivo
with open("my_notes.txt","w") as file:

    file.write("Hola, soy Anayely.\n")# Se escribe tres lineas de notas personales
    file.write("Me gusta mucho la naturaleza.\n")
    file.write("Tambien amo ver los animalitos en su habitat natural.\n")
#Se abre el archivo
#Realizamos la lectura del archivo
with open("my_notes.txt", "r") as file:
    for line in file:#leemos linea por linea
        print(line.strip())