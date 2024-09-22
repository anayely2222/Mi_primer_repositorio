#Crear una función llamada calcular_descuento que tome dos parametros : el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).

def calcular_descuento(monto_total, porcentaje_descuento=10):#función para calcular_descuento
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

#Función para calcular de manera dinamica y que muestre los resultados corrresponcientes

def main():# Se crea la función principal
    #Se le solicita al usuario el monto de la primera compra
    monto_tot = float(input("Ingresa el monto total de la primera compra: "))


    descuento1 = calcular_descuento(monto_tot)
    monto_final1 = monto_tot - descuento1
    print(f"Monto total: ${monto_tot:.2f}, Descuento: ${descuento1:.2f}, Monto final: ${monto_final1:.2f}")

    # Se le solicita al usuario el monto total y el porcentaje de descuento
    monto_tot2 = float(input("Ingrese el monto total de la segunda compra: "))
    porcentaje_descuento2 = float(input("Ingrese el porcentaje de descuento requerido: "))


    descuento2 = calcular_descuento(monto_tot2, porcentaje_descuento2)
    monto_final2 = monto_tot2 - descuento2
    print(f"Monto total: ${monto_tot2:.2f}, Descuento: ${descuento2:.2f}, Monto final: ${monto_final2:.2f}")



if __name__ == "__main__":
    main()
