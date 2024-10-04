contatos = {"priscila@gmail.com": {"nome": "Priscila", "telefone": "3333-2221"}}

resultado = contatos.pop("priscila@gmail.com")  # {'nome': 'Priscila', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("priscila@gmail.com", {})  # {}
print(resultado)