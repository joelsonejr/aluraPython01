import random

def validateUserGuess(guess):
  if guess < 1 or guess > 100:
      while guess < 1 or guess > 100:
          print("\n Seu palpite deve ser um número entre 1 e 100 \n")
          guess = grabUserGuess()
  else:
      return guess
  return guess

def printWrongGuessMessage(guessType):
    print("Você errou. O seu chute foi", guessType , "do que o número secreto")

def grabUserGuess():
    guess = int(input("Digite o seu número: "))
    return guess

def verifyUserGuess(guess):
    print("\n Você digitou: ", guess)

    if (secret_number == guess) :
        return 1
    elif (secret_number < guess):
        return 0
    else:
        return 2

def printResults(evaluatedGuess, maxAttempts, numberOfAttempts):
  if evaluatedGuess == 1:
    print("Você acertou")  
    numberOfAttempts = maxAttempts + 1
    return numberOfAttempts
  elif evaluatedGuess == 0:
    printWrongGuessMessage("maior")
    return numberOfAttempts
  else:
    printWrongGuessMessage("menor")
    return numberOfAttempts

welcomeMessage = "Bem vindo ao jogo de Adivinhação!" 
goodBayMessage = "Fim de jogo. O número secreto era:"
def printGameHeader(message, mode):
  print("*************************************")
  print(message, mode)
  print("*************************************")

secret_number = random.randint(1, 100)

def guessingGame():
  rounds = 1
  max_attempts = 9
  numberOfAttempts = 1

  printGameHeader(welcomeMessage, "")

  while numberOfAttempts <= max_attempts:

    print("Tentativa {} de {}".format(numberOfAttempts,max_attempts))

    user_guess = grabUserGuess()

    user_guess = validateUserGuess(user_guess)

    guessResult = verifyUserGuess(user_guess)

    numberOfAttempts = printResults(guessResult, max_attempts, numberOfAttempts)

    numberOfAttempts += 1

def endGame():
  printGameHeader(goodBayMessage, secret_number)

def run():

  guessingGame()

  endGame()

run()
