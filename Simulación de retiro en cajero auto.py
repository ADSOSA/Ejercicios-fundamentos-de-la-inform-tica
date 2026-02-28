# Simulación de retiro en cajero automático
saldo_disponible = 1500 # Saldo inicial
pin_correcto = "2026"

ingreso_pin = input("Ingrese su PIN: ")

if ingreso_pin == pin_correcto:
    # Solicitar monto y convertir a decimal (float)
    monto_retiro = float(input("Monto a retirar: $"))
    
    if monto_retiro <= saldo_disponible:
        # Proceso de actualización de saldo
        saldo_disponible -= monto_retiro
        print("Transacción exitosa. Tome su dinero.")
        print(f"Su saldo restante es: ${saldo_disponible}")
    else:
        print("Transacción fallida: Fondos insuficientes.")
else:
    print("PIN incorrecto. Acceso denegado.")

print("No olvide retirar su tarjeta.")