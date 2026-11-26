print("Vamos a ver en que categoria pelearias segun tu peso")
print("Aqui te dejo una rubrica según los pesos:\n Menos de 50Kg - Peso mosca.\n De 50 a 60Kg - Peso pluma.\n De 60 a 70Kg - Peso ligero.\n De 70 a 90Kg - Peso pesado.\n Otros - Sin categoria.")
peso = float(input("Indica tu peso: "))
if peso < 50:
    print("Estas en peso mosca.")
elif peso >= 50 and peso < 60:
    print("Estas en peso pluma.")
elif peso >= 60 and peso < 70:
    print("Estas en peso ligero")
elif peso >= 70 and peso < 90:
    print("Estas en peso pesado")
elif peso > 90:
    print("No tienes categoria")