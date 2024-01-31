from os import system, listdir

class CLIGravidade:
  script_gravidade = "./gravidade"
  dir_presets = "./presets/"
  dir_data = "./data/"
  
  def rodar (self, modo:str, arg:str):
    system(f'{self.script_gravidade} {modo} {arg}')
  
  def sorteio (self, arg):
    self.rodar('-s', self.dir_presets + arg)
  
  def sorteio_salvar (self, arg):
    self.rodar('-sv', self.dir_presets + arg)
  
  def vi (self, arg):
    self.rodar('-vi', self.dir_presets + arg)

  def exibir (self, arg):
    self.rodar('-e', self.dir_data + arg)

  def listar_presets (self):
    return listdir(self.dir_presets)

  def filtrar_arquivos (self, tipo:str):
    # Lista os presets
    arquivos_preset = self.listar_presets()
    # Agora filtra por tipo
    presets_tipo = []
    for arquivo in arquivos_preset:
      with open(f"{self.dir_presets}/{arquivo}", 'r') as arq:
        linhas = arq.read().split('\n')
        # O modo esta na segunda linha
        modo = linhas[1].split()[1]
        if modo == tipo:
          presets_tipo.append(arquivo)
    return presets_tipo

  def lista_presets_sorteio (self):
    return self.filtrar_arquivos('sorteio')

  def lista_presets_vi (self):
    return self.filtrar_arquivos('vi')

  def listar_data (self):
    return listdir(self.dir_data)