#     # software bancario simple
#     # depositar y retirar


# Saldo de la primera cuenta

sw = False
while (not sw):
    
    try:

        saldo = input("Bienvenido/a, digite su saldo en la cuenta 1: ")

        valid_salde = float(saldo)

        if valid_salde < 0:
            print("El saldo a introducir debe ser mayor que 0")
            continue

        else:
            sw = True

    except ValueError:
        print("Porfavor ingrese un saldo valido")
        continue

print("Su saldo en la cuenta 1 es: ", saldo)

# Saldo de la segunda cuenta

sb = False
while (not sb):
    
    try:

        saldo2 = input("Bienvenido/a, digite su saldo en la cuenta 2: ")

        valid_salde2 = float(saldo2)

        if valid_salde2 < 0:
            print("El saldo a introducir debe ser mayor que 0")
            continue

        else:
            sb = True

    except ValueError:
        print("Porfavor ingrese un saldo valido")
        continue

print("Su saldo en la cuenta 2 es: ", saldo2)


# Hasta aqui estan los saldos de las cuentas validando que sean numeros

# Transaccion en la cuenta 1 

    
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