def jogada(origem, destino):
    if len(pinos[origem-1]) > 0:
        aux = pinos[origem-1].pop()
        if len(pinos[destino-1]) == 0:
            pinos[destino-1].append(aux)
        elif len(pinos[destino-1]) > 0:
            if aux < (pinos[destino-1][-1]):
                pinos[destino-1].append(aux)
            else:
                pinos[origem-1].append(aux)
                print("Jogada Invalida!")
    else:
        print("Jogada Invalida!")


def mostrarPinos():
    print(pinos[0], "Estes são os pinos na torre 1!")
    print(pinos[1], "Estes são os pinos na torre 2!")
    print(pinos[2], "Estes são os pinos na torre 3!")


pinos = []

for i in range(0, 3):
    pinos.append([])

pinos[0] = [3, 2, 1]

while pinos[2] != [3, 2, 1]:
    mostrarPinos()
    o = int(input("Origem:"))
    d = int(input("Destino:"))
    jogada(o, d)
    print("-" * 150, "\n")
print("Parabens!")
