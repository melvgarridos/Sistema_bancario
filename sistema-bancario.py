#     # software bancario simple
#     # Si coloco una letra no se puede dañar
#     # depositar y retirar

sw = False
while (not sw):
    try:

        saldo = input("Bienvenido/a, digite su saldo: ")

        valid_salde = float(saldo)
        if valid_salde < 0:
            print("El saldo a introducir debe ser mayor que 0")
            continue
        else:
            sw = True
    except ValueError:
        print("Porfavor ingrese un saldo valido")
        continue

print("Su saldo es: ", saldo)
    
proceso = 0

while proceso !=  4:

    proceso = int(input("""
                    Bienvenido/a
                    Por favor ingrese el tipo de transacción desea realizar hoy.

                    1. Retirar saldo
                    2. Agregar Saldo
                    3. Salir    
                        
                        Digite aquí la opción: """))

        
    if proceso == 1:
        retiro = float(input("Por favor digite el total a retirar: "))

        if retiro > valid_salde:
         print("El monto a retirar no puede ser mayor al saldo")

        elif retiro <= valid_salde:
            saldo_final = valid_salde - retiro
            print("Su saldo final es: ", saldo_final)

        proceso = 4

    elif proceso == 2:
        deposito = float(input("Por favor digite el total a depositar: "))
        saldo_final = valid_salde + deposito
        print("Su saldo final es: ", saldo_final)

        proceso = 4

    elif proceso == 3:
        proceso = 4

    else:
        print("Error. Intente nuevamente")


    
print("Proceso finalizado.")