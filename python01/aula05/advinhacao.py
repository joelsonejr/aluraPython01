print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = 42
max_attempts = 3
rounds = ""

for rounds in range(1, max_attempts + 1):

    print("Tentativa {} de {}".format(rounds,max_attempts))

    user_guess = int(input("Digite o seu número: "))

    print("Você digitou: ", user_guess)

    guessed_correctly = secret_number == user_guess
    guessed_more = secret_number < user_guess
    guessed_less = secret_number > user_guess



    if guessed_correctly:
        print("Você acertou")
        break

    else:
        if guessed_more:
            print("Você errou. O seu chute foi maior do que o número secreto")
        elif guessed_less:
            print("Você errou. O seu chute foi menor do que o número secreto")

