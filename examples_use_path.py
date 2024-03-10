import os
from pathlib import Path

print()
print(os.path.dirname(__file__))
print()

# Obter o caminho especificado no parametro
path_especificado = Path(os.path.abspath('src'))

# Obter o caminho absoluto do arquivo atual
caminho_atual = os.path.dirname(__file__)

# Voltar um diretório para trás
um_diretorio_atras = os.path.dirname(caminho_atual)

# Voltar dois diretórios para trás
dois_diretorios_atras = os.path.dirname(um_diretorio_atras)

print()
print("Caminho do diretório atual:", caminho_atual)
print()
print("Caminho do diretório um diretório atrás:", um_diretorio_atras)
print()
print("Caminho do diretório dois diretórios atrás:", dois_diretorios_atras)
print()
print()
print()
print()
print(path_especificado)