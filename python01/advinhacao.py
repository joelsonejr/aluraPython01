import random

print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = random.randrange(1, 101)
max_attempts = 3
rounds = ""
points = 1000

print("Selecione o nível de dificuldade desejado: ")
print("(1) Fácil (2) Médio (3) Difícil")

gameDificulty = int(input("Nível de dificuldade: "))

if (gameDificulty == 1):
    max_attempts = 10
elif (gameDificulty == 2):
        max_attempts = 5
else:
    max_attempts = 3


for rounds in range(1, max_attempts + 1):

    print("Tentativa {} de {}".format(rounds,max_attempts))

    user_guess = int(input("Digite o seu número: "))

    if user_guess <= 0:
        while user_guess < 1 or user_guess > 100:
            print("\n Seu palpite deve ser um número entre 1 e 100 \n")
            user_guess = int(input("Digite o seu número: \n"))

    print("\n Você digitou: ", user_guess)

    guessed_correctly = secret_number == user_guess
    guessed_more = secret_number < user_guess
    guessed_less = secret_number > user_guess

    if guessed_correctly:
        print("Você acertou e fez {} pontos".format(points))
        break

    else:
        if guessed_more:
            print("Você errou. O seu chute foi maior do que o número secreto")
        elif guessed_less:
            print("Você errou. O seu chute foi menor do que o número secreto")
        
        lostPoints = abs(secret_number - user_guess)
        points = points - lostPoints



