notas = []

cantidad = int(input("ingrese cantidad de notad a promediar: "))
for i in range(cantidad):
    nota = float(input(f"ingrese nota numero {1 + i}: "))
    notas.append(nota)
    
resolver = sum(notas) / len(notas)
print(f"el promedio de tus notas es {resolver}")