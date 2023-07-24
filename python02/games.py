import forca
import advinhacao

def playGames():
  print("*********************************")
  print("Bem vindo ao jogos em Python!!!")
  print("Qual jogo você gostaria de jogar?")
  print("*********************************")
  print("(1) - Forca (2) Adivinhação")
  print("*********************************")

  selectedGame = int(input("Jogo selecionado: "))

  while(selectedGame != 1 and selectedGame != 2 and selectedGame != 3):
    print("O número selecionado deve ser entre 1 e 3")
    selectedGame = int(input("Jogo selecionado: "))

  if(selectedGame == 1): 
      print("Você selecionou o jogo de Forca")
      forca()
  elif(selectedGame == 2):
      print("Você selecionou o jogo de Adivinhação")
      advinhacao.playAdivinhacao()
  else:
      print("Saindo do jogo ...")

# runs the program when it's executed directly from terminal, and not whem it's imported by another script.
if __name__ == "__main__":
   playGames()


