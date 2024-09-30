#Crear un diccionario que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".
#En el cual el nombre sera Yael , su edad de 24 ,su ciudad es San Jose y su profesion es Arquitecto.
informacion_personal={
    "Nombre":"Yael",
    "Apellido":"Rodriguez",
    "Edad":24,
    "Estatura":1.70,
    "Ciudad":"San Jose",
    "Profesión":"Arquitecto"
}
#Se accede y modifica la ciudad de la persona.
informacion_personal["Ciudad"]="Joya de los Sachas"#se cambia de ciudad
#Agregar una nueva clave-valor que sea profesión ,pero como ya tenemos la profesión solo se actualizara
informacion_personal["Profesión"]= "Médico"
#Se agregó un número de teléfono ficticio
if "Teléfono" not in informacion_personal:
    informacion_personal["Teléfono"] = "0990439567"
#
del informacion_personal["Edad"] # Se elimina la clave "edad" del diccionario

print("Diccionario Final:",informacion_personal)