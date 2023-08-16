def playForca():
  print("*********************************")
  print("   Bem vindo ao jogo de Forca!   ")
  print("*********************************")

  secret_word = "banana"

  hanged = 0
  hitted = False
  guessed_letter = []

  for i in range(len(secret_word)):
    guessed_letter.append("_")

  print(guessed_letter)

  while(hanged <= 6 and not hitted ):
    hanged = 0
    
    guess = (input("Qual a letra? "))
    guess = guess.strip()

    index = 0

    for letter in secret_word:
      if(letter.lower() == guess.lower()):
        print("Encontrei a letra {} na posição {}".format(guess, index))
        guessed_letter[index] = letter

      index = index + 1

    print(guessed_letter)
    
    def finishGame(guess, secret_word):
      guess = ''.join(guess)
      
      if(guess == secret_word):
        print("Parabéns, você acertou!!!! A palavra secreta era {0}".format(secret_word))
      else:
        (print("Tente novamente"))
      hanged = hanged + 1

    finishGame(guessed_letter, secret_word)
  
  print("Fim do jogo")

# runs the program when it's executed directly from terminal, and not whem it's imported by another script.
if __name__ == "__main__":
  playForca()