# Lembre-se de alterar o caminho do arquivo, para o caminho completo da sua máquina!

arquivo = open(
    "/home/pri/pjs/ENGENHARIA_DADOS_NTT/6.Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.read())
arquivo.close()

arquivo = open(
    "/home/pri/pjs/ENGENHARIA_DADOS_NTT/6.Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readline())
arquivo.close()

arquivo = open(
    "/home/pri/pjs/ENGENHARIA_DADOS_NTT/6.Manipulação de arquivos/lorem.txt", "r"
)
print(arquivo.readlines())
arquivo.close()

arquivo = open(
   "/home/pri/pjs/ENGENHARIA_DADOS_NTT/6.Manipulação de arquivos/lorem.txt", "r"
)
# tip
while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()