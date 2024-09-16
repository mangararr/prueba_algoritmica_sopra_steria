def clasificar_personas(archivo):
    mayores_edad = 0
    menores_edad = 0
    masculinos_mayores = 0
    femeninas_menores = 0
    personas = []

    with open(archivo, 'r') as f:
        for linea in f:
            edad, sexo = linea.strip().split(',')
            edad = int(edad)
            personas.append(f"Persona: {edad} años, {sexo}")

            if edad >= 18:
                mayores_edad += 1
                if sexo == "Masculino":
                    masculinos_mayores += 1
            else:
                menores_edad += 1
                if sexo == "Femenino":
                    femeninas_menores += 1

    num_personas = len(personas)
    porcentaje_mayores = (mayores_edad / num_personas) * 100
    porcentaje_mujeres = (sum(1 for persona in personas if "Femenino" in persona) / num_personas) * 100

    return mayores_edad, menores_edad, masculinos_mayores, femeninas_menores, porcentaje_mayores, porcentaje_mujeres, personas

while True:
    comando = input("Escribe LEER PERSONAS para abrir un archivo: ")
    if comando.upper() == "LEER PERSONAS":
        archivo_personas = input("Ingresa el nombre del archivo: ")
        try:
            mayores, menores, masculinos_mayores, femeninas_menores, porcentaje_mayores, porcentaje_mujeres, lista_personas = clasificar_personas(archivo_personas)

            print("Lista de personas:")
            for persona in lista_personas:
                print(persona)

            print(f"\nPersonas mayores de edad: {mayores} ({porcentaje_mayores:.2f}%)")
            print(f"Personas menores de edad: {menores} ({100 - porcentaje_mayores:.2f}%)")
            print(f"Hombres mayores de edad: {masculinos_mayores}")
            print(f"Mujeres menores de edad: {femeninas_menores}")
            print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")

        except FileNotFoundError:
            print("El archivo no existe. Por favor, verifica el nombre.")
    else:
        print("Comando inválido. Escribe LEER PERSONAS para continuar.")
