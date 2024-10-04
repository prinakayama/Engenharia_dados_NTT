contatos = {"priscila@gmail.com": {"nome": "Priscila", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('priscila@gmail.com', {'nome': 'Priscila', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError