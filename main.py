import random


def dados(quantidade):
  vitorias = 0
  controles = 0
  nada = 0
  entropias = 0
  
  for i in range(quantidade):
    dado = random.randint(1,6)
    match dado:
      case 1:
        entropias = entropias + 1
      case 2 | 3:
        nada = nada +1
      case 4 | 5 :
        controles = controles + 1
      case 6 :
        vitorias = vitorias + 1
      case _ :
        return

  print(
    "Vitórias: ", vitorias,
    "\nControles: ", controles,
    "\nNada: ", nada,
    "\nEntropias: ", entropias 
  )
'''
implementar função de reroll. Input? Criar dicionário com os valores do resultado?
def reroll(resultado):
  match resultado:
    case "Vitórias":
'''
  
dados(5)