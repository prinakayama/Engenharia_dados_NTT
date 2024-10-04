contato = {"nome": "Priscila", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Priscila"
print(contato)  # {'nome': 'Priscila', 'telefone': '3333-2221'}

contato.setdefault("idade", 40)  # 40
print(contato)  # {'nome': 'Priscila', 'telefone': '3333-2221', 'idade': 40}