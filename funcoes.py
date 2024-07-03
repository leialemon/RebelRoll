import random


def dados(quantidade):
  global resultado
  resultado = {
    "vitorias" : 0,
    "controles" : 0,
    "nada" : 0,
    "entropias" : 0
  }
  
  
  for i in range(quantidade):
    dado = random.randint(1,6)
    match dado:
      case 1:
        resultado["entropias"] = resultado["entropias"] + 1
      case 2 | 3:
        resultado["nada"] = resultado["nada"] + 1
      case 4 | 5 :
        resultado["controles"] = resultado["controles"] + 1
      case 6 :
        resultado["vitorias"] = resultado["vitorias"] + 1
      case _ :
        return

  return resultado
  
  
'''
  return(
    "Vitórias: ", vitorias,
    "\nControles: ", controles,
    "\nNada: ", nada,
    "\nEntropias: ", entropias 
  )
  '''
'''
implementar função de reroll. Input? Criar dicionário com os valores do resultado?
def reroll(resultado):
  match resultado:
    case "Vitórias":
'''
  
