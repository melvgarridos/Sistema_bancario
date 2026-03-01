#     # software bancario simple
#     # depositar y retirar


# Saldo de la primera cuenta

sw = False
while (not sw):
    
    try:

        saldo = input("""
            Bienvenido(a) a nuestra entidad financiera.

            Para continuar con la operación, por favor ingrese el saldo actual disponible en la Cuenta 1.

            Digite el valor correspondiente a continuación: """)

        valid_saldo = float(saldo)

        if valid_saldo < 0:
            print("El valor ingresado debe ser mayor a cero (0) para poder continuar con la operación. Por favor, verifique e intente nuevamente.")
            continue

        else:
            sw = True

    except ValueError:
        print("""El valor ingresado no es válido.

                Por favor, verifique la información suministrada e ingrese un saldo válido para continuar con la operación.""")
        continue

print("El saldo disponible en la Cuenta 1 es: ", saldo)

# Saldo de la segunda cuenta

sb = False
while (not sb):
    
    try:

        saldo2 = input("""
            Bienvenido(a) a nuestra entidad financiera.

            Para continuar, por favor ingrese el saldo actual disponible en la Cuenta 2.

            Digite el valor correspondiente a continuación: """)

        valid_saldo2 = float(saldo2)

        if valid_saldo2 < 0:
            print("El valor ingresado debe ser mayor a cero (0) para poder continuar con la operación. Por favor, verifique e intente nuevamente.")
            continue

        else:
            sb = True

    except ValueError:
        print("El valor ingresado no es válido. Por favor, verifique la información suministrada e ingrese un saldo válido para continuar con la operación.")
        continue

print("El saldo disponible en la Cuenta 2 es: ", saldo2)

saldo_total = valid_saldo + valid_saldo2

# Hasta aqui estan los saldos de las cuentas validando que sean numeros


    
ta = 0
while ta !=  4:

    tipo_transaccion = input("""
    Por favor seleccione el tipo de transacción que desea realizar:

        1. Retiro de fondos
        2. Depósito de fondos
        3. Salir del sistema

        Digite el número correspondiente a la opción deseada para continuar: """)
    
    try:
        transaccion_valida = int(tipo_transaccion)
    except ValueError:
        print("La opción ingresada no es válida. Por favor, ingrese un número correspondiente a una de las opciones disponibles.")
        continue

    # Retirar dinero
        
    if transaccion_valida == 1:

# tipo de cuenta

            tipo_cuenta = input("""
                Por favor, seleccione la cuenta de la cual desea realizar el retiro de fondos:
                1. Cuenta 1
                2. Cuenta 2
                Digite el número correspondiente a la opción deseada para continuar: """)
            
            try:
                tipo_cuenta = int(tipo_cuenta)
            except ValueError:
                print("La opción ingresada no es válida. Por favor, ingrese un número correspondiente a una de las opciones disponibles.")
                continue

            if tipo_cuenta == 1:

                retiro = input("Por favor, ingrese el valor exacto que desea retirar de su cuenta para continuar con la operación: ")
                
                try:
                    retiro_valido = float(retiro)
                except ValueError:
                    print("El valor ingresado no es válido. Por favor, ingrese un número correspondiente al monto que desea retirar.")
                    continue
                
                impuesto = retiro_valido * 0.004

                total_retiro = retiro_valido + impuesto

                if retiro_valido == valid_saldo:

                    confirmacion = input("""
                            ¿Desea realizar el retiro total del saldo disponible en su cuenta?

                            Le informamos que esta transacción está sujeta al Gravamen a los Movimientos Financieros (4x1000), el cual se aplicará sobre el monto a retirar y será debitado junto con la operación correspondiente.

                            Por favor, confirme su decisión:

                            1. Sí, deseo continuar con el retiro total del saldo disponible.

                            2. No, deseo cancelar la operación.

                            Seleccione una opción para continuar: """)
                    
                    try: confirmacion = int(confirmacion)
                    except ValueError:  
                        print("La opción ingresada no es válida. Por favor, ingrese un número correspondiente a una de las opciones disponibles.")
                        continue

                    if confirmacion == 1:

                        saldo_final = saldo_total - total_retiro

                        print("Total del retiro: ", total_retiro)
                        print("Su saldo final en la cuenta 2 es: ", saldo_final)

                    elif confirmacion == 2:

                        print("Transacción cancelada, por favor intente nuevamente")

                    else:
                        print("La opción ingresada no es válida. Por favor, ingrese un número correspondiente a una de las opciones disponibles.")
                        continue
                        

                elif total_retiro > valid_saldo:

                    print("No tiene suficiente saldo para realizar esta transacción, por favor intente nuevamente")

                elif total_retiro <= valid_saldo:

                    saldo_final = saldo_total - total_retiro

                    print("Total del retiro: ", total_retiro)
                    print("Su saldo final en la cuenta 1 es: ", saldo_final)

                else: 
                        print("El valor ingresado no es válido. Por favor, ingrese un número correspondiente al monto que desea retirar.")
                        continue


                ta = 4
        
            elif tipo_cuenta == 2:

                retiro = input("Por favor, ingrese el valor exacto que desea retirar de su cuenta para continuar con la operación: ")
                
                try:
                    retiro_valido = float(retiro)
                except ValueError:
                    print("El valor ingresado no es válido. Por favor, ingrese un número correspondiente al monto que desea retirar.")
                    continue
                
                impuesto = retiro_valido * 0.004

                total_retiro = retiro_valido + impuesto

                if retiro_valido == valid_saldo2:

                    confirmacion = input("""
                            ¿Desea realizar el retiro total del saldo disponible en su cuenta?

                            Le informamos que esta transacción está sujeta al Gravamen a los Movimientos Financieros (4x1000), el cual se aplicará sobre el monto a retirar y será debitado junto con la operación correspondiente.

                            Por favor, confirme su decisión:

                            1. Sí, deseo continuar con el retiro total del saldo disponible.

                            2. No, deseo cancelar la operación.

                            Seleccione una opción para continuar: """)
                    
                    try: confirmacion = int(confirmacion)
                    except ValueError:  
                        print("La opción ingresada no es válida. Por favor, ingrese un número correspondiente a una de las opciones disponibles.")
                        continue

                    if confirmacion == 1:

                        saldo_final = saldo_total - total_retiro

                        print("Total del retiro: ", total_retiro)
                        print("Su saldo final en la cuenta 1 es: ", saldo_final)

                    elif confirmacion == 2:

                        print("Transacción cancelada, por favor intente nuevamente")
                        continue

                    else:
                        print("La opción ingresada no es válida. Por favor, ingrese un número correspondiente a una de las opciones disponibles.")
                        continue
                        

                elif total_retiro > valid_saldo2:

                    print("No tiene suficiente saldo para realizar esta transacción, por favor intente nuevamente")

                elif total_retiro <= valid_saldo2:

                    saldo_final = valid_saldo2 - total_retiro

                    print("Total del retiro: ", total_retiro)
                    print("Su saldo final en la cuenta 2 es: ", saldo_final)

                else: 
                        print("El valor ingresado no es válido. Por favor, ingrese un número correspondiente al monto que desea retirar.")
                        continue


                ta = 4
            
# depositar dinero
    elif transaccion_valida == 2:

            numero_cuenta = input("""
                Por favor, seleccione la cuenta a la cual desea realizar el depósito:
                1. Cuenta 1
                2. Cuenta 2 
                Digite el número correspondiente a la opción deseada para continuar: """)
            
            # tipo de cuenta

            
            try:
                numero_cuenta = int(numero_cuenta)
            except ValueError:
                print("La opción ingresada no es válida. Por favor, ingrese un número correspondiente a una de las opciones disponibles.")
                continue
            
            if numero_cuenta == 1:
            
                deposito = input("Por favor digite el monto total a depositar: ")
                try:
                    deposito = float(deposito)
                except ValueError:
                    print("El valor ingresado no es válido. Por favor, ingrese un número correspondiente al monto que desea depositar.")
                    continue
                saldo_final = valid_saldo + deposito
                print("Su saldo final en la cuenta 1 es: ", saldo_final)

            elif numero_cuenta == 2:

                deposito = input("Por favor digite el monto total a depositar: ")
                try:
                    deposito = float(deposito)
                except ValueError:
                    print("El valor ingresado no es válido. Por favor, ingrese un número correspondiente al monto que desea depositar.")
                    continue
                saldo_final = valid_saldo2 + deposito
                print("Su saldo final en la cuenta 2 es: ", saldo_final)
            
            else:
                print("Error. Intente nuevamente")
                continue

            ta = 4
# salir del sistema
    elif transaccion_valida == 3:
        ta = 4

    else:
        print("Error. Intente nuevamente")
        continue


    
print("Proceso finalizado.")