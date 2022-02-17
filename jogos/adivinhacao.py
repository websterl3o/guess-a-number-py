import random
print("================================")
print("Bem Vindo ao Jogo de Advinhação")
print("================================")

numero_range = 10
numero_secreto = random.randint(0,numero_range)
numero_max_tentativas = 3
numero_tentativa = 1
numero_pontos = 100

print("*R:Numero Secreto = {}".format(numero_secreto))

print("Qual o nivel de dificuldade?")
print("(1) Facil - (2) Medio - (3) Dificil")

dificuldade = int(input("Dificuldade: "))
if dificuldade == 1:
    numero_max_tentativas = 15
elif dificuldade == 2:
    numero_max_tentativas = 7
else:
    numero_max_tentativas = 3

for rodada in range(1, numero_max_tentativas + 1):
    print("\n--------------------------------")
    print("Tentativa {} de {}".format(rodada, numero_max_tentativas))
    print("--------------------------------\n")
    numero_inserido = int(input("Digite o seu numero entre {} e {}: ".format(0,numero_range)))

    print("Voce digitou: ", numero_inserido)

    if(numero_inserido < 0 or numero_inserido > 100):
        print("*Voce digitou um numero invalido!")
        print("*Precisa ser um numero {} e {}!!".format(0,numero_range))
        continue

    acertou = numero_inserido == numero_secreto

    if (acertou):
        print("\n+++++++++++++++++++++++++++++++++++++")
        print("=====================================")
        print("Parabens, Voce Acertou!! B)")
        print("=====================================")
        print("+++++++++++++++++++++++++++++++++++++\n")
        break
    else:
        chute_maior = numero_inserido > numero_secreto
        chute_menor = numero_inserido < numero_secreto

        if (chute_maior):
            print("Voce errou! O seu chute foi maior que o numero secreto.")
            numero_pontos -=
        elif (chute_menor):
            print("Voce errou! O seu chute foi menor que o numero secreto.")
print("Fim de Jogo ;D")
