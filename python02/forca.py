import random

def jogar():
    
  print_welcome_message()

  palavra_secreta = create_secret_word()

  letras_acertadas = initialize_guessing_board(palavra_secreta)
  print(letras_acertadas)

  print(palavra_secreta)

  enforcou = False
  acertou = False
  erros = 0

  while(not enforcou and not acertou):

      chute = ask_for_guess()

      if (chute in palavra_secreta):
        save_correct_guess(chute, palavra_secreta, letras_acertadas)
      else:
          erros += 1
          print("Errouuuuuuuuuuuuu. Restam {} tentativas.".format(6 - erros))

      enforcou = erros == 6
      acertou = "_" not in letras_acertadas

      print(letras_acertadas)

  if (acertou):
    winner_message()
  else:
    loser_message()
  



def print_welcome_message():
  print("*********************************")
  print("***Bem vindo ao jogo da Forca!***")
  print("*********************************")

def create_secret_word():
  palavras = []
    
  with open("palavras.txt") as arquivo:
    for linha in arquivo:
      linha = linha.strip()
      palavras.append(linha)


    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()

  return palavra_secreta

def initialize_guessing_board(palavra):
  return ["_" for letra in palavra]

def ask_for_guess():
  chute = input("Qual letra? ")
  chute = chute.strip().upper()

  return chute

def save_correct_guess(chute, palavra, letras_acertadas):
  index = 0
  for letra in palavra:
      if(chute == letra):
          letras_acertadas[index] = letra
      index += 1
  

def winner_message():
   print("Você ganhou")

def loser_message():
   print("Você perdeu")

if(__name__ == "__main__"):
    jogar()