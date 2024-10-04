contatos = {"priscila@gmail.com": {"nome": "Priscila", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["priscila@gmail.com"] = {"nome": "Pri"}

print(contatos["priscila@gmail.com"])  # {"nome": "Priscila", "telefone": "3333-2221"}

print(copia["priscila@gmail.com"])  # {"nome": "Pri"}