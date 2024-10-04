contatos = {"priscila@gmail.com": {"nome": "Priscila", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "priscila@gmail.com", {}
)  # {"priscila@gmail.com": {"nome": "Priscila", "telefone": "3333-2221"}
print(resultado)