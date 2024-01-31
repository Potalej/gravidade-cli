from simple_term_menu import TerminalMenu
from cli import CLIGravidade
import os

def main ():
  # As primeiras opcoes sao de acao. Quer qual?
  opcoes_acao = [
    "Exibir trajetórias", 
    "Gerar preset de valores iniciais",
    "Simular",
    "Sair"
  ]
  terminal_menu = TerminalMenu(opcoes_acao, title="Escolha o que fazer:")
  menu_index_acao = terminal_menu.show()

  menu = Menu()

  # Escolhida a acao, precisa ver o que fazer agora
  if menu_index_acao == 0:
    menu.exibir_trajetorias()
  elif menu_index_acao == 1:
    menu.gerar_preset_vi()
  elif menu_index_acao == 2:
    menu_simular()
  else:
    return

  main()

class Menu:
  cli = CLIGravidade()
  
  def exibir_trajetorias(self):
    data = self.cli.listar_data()
    if len(data) == 0:
      print("Não há simulações salvas. Voltando para o início.")
      return 

    terminal = TerminalMenu(data, title="Escolha a simulação para visualizar:")
    indice = terminal.show()

    print(f"A simulação escolhida foi: {data[indice]}.\nExibindo...\n")
    cli.exibir(data[indice])

  def gerar_preset_vi (self):
    presets_sorteio = self.cli.lista_presets_sorteio()
    if len(presets_sorteio) == 0:
      print("Não há presets salvos. Voltando para o início.")
      return
      
    terminal = TerminalMenu(presets_sorteio, title="Escolha o preset para sortear valores iniciais:")
    indice = terminal.show()

    print(f"O preset escolhido foi: {presets_sorteio[indice]}.\nGerando...\n")
    self.cli.sorteio_salvar(presets_sorteio[indice])

if __name__ == "__main__":
  main()