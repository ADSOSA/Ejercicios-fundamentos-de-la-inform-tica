# Simulación de inscripción universitaria
print("--- Sistema de Inscripción Universitaria ---")
continuar = "si"

while continuar.lower() == "si":
    materia = input("Nombre de la materia a inscribir: ")
    cupos = int(input(f"Ingrese cupos actuales para {materia}: "))
    
    if cupos > 0:
        print(f"¡Felicidades! Ha quedado inscrito en {materia}.")
    else:
        print(f"Lo sentimos, no hay cupos para {materia}.")
    
    continuar = input("\n¿Desea inscribir otra materia? (si/no): ")

print("\nProceso terminado. Su hoja de inscripción ha sido generada.")
