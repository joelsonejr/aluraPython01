def playForca():
  print("*********************************")
  print("  Bem vindo ao jogo de Forca!")
  print("*********************************")

  secret_word = "banana"

  hanged = False
  hitted = False
  guessed_letter =[]

  for i in range(len(secret_word)):
    guessed_letter.append("_")

  print(guessed_letter)

  while(not hanged and not hitted):
    guess = (input("Qual a letra? "))
    guess = guess.strip()

    index = 0

    for letter in secret_word:
      if(letter.lower() == guess.lower()):
        print("Encontrei a letra {} na posição {}".format(guess, index))
        guessed_letter[index] = letter

      index = index + 1

    print(guessed_letter)
  
  print("Fim do jogo")

# runs the program when it's executed directly from terminal, and not whem it's imported by another script.
if __name__ == "__main__":
  playForca()