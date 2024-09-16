import random

def clasificar_personas(num_personas):
    mayores_edad = 0
    menores_edad = 0
    masculinos_mayores = 0
    femeninas_menores = 0
    personas = []

    for i in range(num_personas):
        edad = random.randint(1, 50)
        sexo = random.choice(["Masculino", "Femenino"])
        
        personas.append(f"Persona {i+1}: {edad} años, {sexo}")

        if edad >= 18:
            mayores_edad += 1
            if sexo == "Masculino":
                masculinos_mayores += 1
        else:
            menores_edad += 1
            if sexo == "Femenino":
                femeninas_menores += 1
                
    porcentaje_mayores = (mayores_edad / num_personas) * 100
    porcentaje_mujeres = (sum(1 for persona in personas if "Femenino" in persona) / num_personas) * 100

    return mayores_edad, menores_edad, masculinos_mayores, femeninas_menores, porcentaje_mayores, porcentaje_mujeres, personas

num_personas = 50
mayores, menores, masculinos_mayores, femeninas_menores, porcentaje_mayores, porcentaje_mujeres, lista_personas = clasificar_personas(num_personas)

print("Lista de personas:")
for persona in lista_personas:
    print(persona)

print(f"\nPersonas mayores de edad: {mayores} ({porcentaje_mayores:.2f}%)")
print(f"Personas menores de edad: {menores} ({100 - porcentaje_mayores:.2f}%)")
print(f"Hombres mayores de edad: {masculinos_mayores}")
print(f"Mujeres menores de edad: {femeninas_menores}")
print(f"Porcentaje de mujeres: {porcentaje_mujeres:.2f}%")
