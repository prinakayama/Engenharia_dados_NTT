arquivo = open(
    "/home/pri/pjs/ENGENHARIA_DADOS_NTT/6.Manipulação de arquivos/teste.txt", "w"
)
arquivo.write("Escrevendo dados em um novo arquivo.")
arquivo.writelines(["\n", "escrevendo", "\n", "um", "\n", "novo", "\n", "texto"])
arquivo.close()