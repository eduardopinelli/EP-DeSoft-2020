import random

dinheiro = 100

print("Bem vindo ao Craps")
print("Você comecará na primeira fase, o Come Out")
gameMode = 0
quer_jogar = True
while dinheiro > 0 and quer_jogar:
    print("Qual tipo de aposta você quer fazer? (se quiser encerrar a partida, digite sair)")
    tipo_aposta = str(input("Pass Line Bet / Field / Any Craps / Twelve\n"
                            ""))
    if tipo_aposta == "sair":
        print("Voce encerrou a partida com {0} dinheiros, até a próxima!".format(dinheiro))
        quer_jogar = False
        break

    valor_aposta = int(input("Quanto você deseja apostar? Saldo disponivel: {0} ".format(dinheiro)))
    if tipo_aposta == "Pass Line Bet":
        dinheiro -= valor_aposta
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        soma = dado_1 + dado_2
        if soma == 7 or soma == 11:
            dinheiro = dinheiro + valor_aposta + 10
            print("Os dados somaram {0}, voce ganhou 10 dinheiros".format(soma))
            continue
        elif soma in [2,3,12]:
            print("Resultado: {0}. Voce perdeu a aposta! Novo saldo: {1}".format(soma, dinheiro))
            continue
        elif soma in [4,5,6,8,9,10]:
            print("A soma dos dados é {0} \n"
                  "Voce avancou para a fase Point, os dados serão lancados novamente e se forem iguais à soma anterior, voce vence".format(soma))
            gameMode = 1
        if gameMode == 1:
             dado_3 = random.randint(1, 6)
             dado_4 = random.randint(1, 6)
             soma2 = dado_3 + dado_4
             while gameMode == 1:
                 if soma2 == soma:
                    print("Resultado: {0}. Voce venceu! Novo saldo: {1}".format(soma2,dinheiro))
                    dinheiro += 2 * valor_aposta
                    gameMode = 0
                    break
                 elif soma2 == 7:
                    print("Resultado: {0}. Voce perdeu tudo! Novo saldo: {1}".format(soma2,dinheiro))
                    gameMode = 0
                    break
                 else:
                     continue
    if tipo_aposta == "Field":
        dinheiro -= valor_aposta
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        soma = dado_1 + dado_2
        if soma in [5,6,7,8]:
            print("Resultado: {0}. Voce perdeu! Novo saldo: {1}".format(soma, dinheiro))
        elif soma in [3,4,9,10,11]:
            dinheiro += 2 * valor_aposta
            print("Resultado: {0}. Voce venceu! Novo saldo: {1}".format(soma, dinheiro))
        elif soma == 2:
            dinheiro += 3 * valor_aposta
            print("Resultado: {0}. Voce venceu! Novo saldo: {1}".format(soma, dinheiro))
        elif soma == 12:
            dinheiro += 4 * valor_aposta
            print("Resultado: {0}. Voce venceu! Novo saldo: {1}".format(soma, dinheiro))

    if tipo_aposta == "Any Craps":
        dinheiro -= valor_aposta
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        soma = dado_1 + dado_2
        if soma in [2,3,12]:
            dinheiro += 8 * valor_aposta
            print("Resultado: {0}. Voce venceu! Novo saldo: {1}".format(soma,dinheiro))
        else:
            print("Resultado: {0}. Voce perdeu! Novo saldo: {1}".format(soma,dinheiro))

    if tipo_aposta == "Twelve":
        dinheiro -= valor_aposta
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        soma = dado_1 + dado_2
        if soma == 12:
            dinheiro += 31 * valor_aposta
            print("Resultado: {0}. Voce venceu! Novo saldo: {1}".format(soma, dinheiro))
        else:
            print("Resultado: {0}. Voce perdeu! Novo saldo: {1}".format(soma,dinheiro))

    if dinheiro == 0:
        print("Voce quebrou a banca! Até a próxima!\nGame Over")








