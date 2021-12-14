def mostraPinos():
    print(pino1, "São os discos do pino1")
    print(pino2, "sao os discos do pino2")
    print(pino3, "sao os discos do pino3")


def linhaTracejada():
    print("-" * 150, '\n')


def jogada(orig, dest):
    if dest == 1:
        if orig != 1:
            if len(pino1) > 0:
                if pino1[-1] > vAuxilar:
                    pino1.append(vAuxilar)
            else:
                pino1.append(vAuxilar)
        else:
            print("movimento invalido!")
            if orig == 1:
                pino1.append(vAuxilar)
            elif orig == 2:
                pino2.append(vAuxilar)
            elif orig == 3:
                pino3.append(vAuxilar)
    elif dest == 2:
        if len(pino2) > 0:
            if pino2[-1] > vAuxilar:
                pino2.append(vAuxilar)
            else:
                print("movimento invalido!")
                if orig == 1:
                    pino1.append(vAuxilar)
                elif orig == 2:
                    pino2.append(vAuxilar)
                elif orig == 3:
                    pino3.append(vAuxilar)
        else:
            pino2.append(vAuxilar)
    elif dest == 3:
        if len(pino3) > 0:
            if pino3[-1] > vAuxilar:
                pino3.append(vAuxilar)
            else:
                print("movimento invalido!")
                if orig == 1:
                    pino1.append(vAuxilar)
                elif orig == 2:
                    pino2.append(vAuxilar)
                elif orig == 3:
                    pino3.append(vAuxilar)
        else:
            pino3.append(vAuxilar)
    return dest, orig


# variaveis
pino1 = [3, 2, 1]
pino2 = []
pino3 = []
vAuxilar = 0
linhaTracejada()
mostraPinos()
while pino3 != [3, 2, 1]:
    origem = int(input("De qual pino deseja retirar o disco? "))
    while origem <= 0 or origem > 3:
        print("Jogada Invalida!")
        origem = int(input("De qual pino deseja retirar o disco:? "))
    if origem == 1:
        if len(pino1) > 0:  # se tiver um valor no pino 1
            vAuxilar = pino1.pop()
        else:
            print("Não tem discos neste pino")
            vAuxilar = 0
    elif origem == 2:
        if len(pino2) > 0:  # se tiver um valor no pino2
            vAuxilar = pino2.pop()
        else:
            print("Não tem discos neste pino")
            vAuxilar = 0
    elif origem == 3:
        if len(pino3) > 0:    # se tiver um valor no pino3
            vAuxilar = pino3.pop()
        else:
            print("Não tem discos neste pino")
            vAuxilar = 0
    if vAuxilar != 0:
        destino = int(input("Para qual pino vai o disco?"))
        while destino > 3 or destino < 1:
            print("Destino invalido!")
            destino = int(input("Para qual pino vai o disco?"))
        linhaTracejada()
        origem, destino = jogada(origem, destino)
        mostraPinos()
        linhaTracejada()

print("Voce Conseguiu! Parabens!!")
