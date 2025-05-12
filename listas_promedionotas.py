notas = []
seguir = True
while seguir:
    nota = int(input("Ingrese nota: "))
    if nota == -1:
        seguir = False
    else:
        notas.append(nota)

print(notas)
print("Promedio: ",round((sum(notas)/len(notas))))
