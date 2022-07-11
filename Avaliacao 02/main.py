from Livro import Livro
from Revista import Revista
from PilhaRevista import PilhaRevista
from PilhaLivro import PilhaLivro
PilhaL = PilhaLivro()
PilhaR = PilhaRevista()


def adicionarLivro(livro):
  livro.adicionar()
  PilhaL.adicionar(livro)

def adicionarRevista(revista):
  revista.adicionar()
  PilhaR.adicionar(revista)


menu = """ 
  ==================================================================
                                MENU    
  ==================================================================
  0- Finalizar o Programa
  
  ========LIVROS========
  
  1- Adicionar um Livro
  2- Remover um Livro
  3- Imprimir os Livros
  
  =======REVISTAS=======
  
  4- Adicionar uma Revista
  5- Remover uma Revista
  6- Imprimir as Revistas
  
  ==================================================================
  --> Digite "EXIT" a qualquer momento para voltar ao menu.
  ==================================================================
  Escolha: """

def MENU():
  n_digit = input(menu)

  if n_digit == '0': exit()

  elif n_digit == '1': adicionarLivro(Livro())
  elif n_digit == '2': PilhaL.remover()
  elif n_digit == '3': PilhaL.imprimir()
  elif n_digit == '4': adicionarRevista(Revista())
  elif n_digit == '5': PilhaR.remover()
  elif n_digit == '6': PilhaR.imprimir()

  else:
    input(' >>> ERRO.  Opção inválida.[ENTER]')
    MENU()
  MENU()

MENU()
