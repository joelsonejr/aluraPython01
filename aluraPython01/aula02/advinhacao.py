print("*********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("*********************************")

secret_number = 42

user_guess = int(input("Digite o seu número: "))

print("Você digitou: ", user_guess)

if secret_number == user_guess:
    print("Você acertou")
else:
    print("Você errou")
