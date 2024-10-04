contatos = {"priscila@gmail.com": {"nome": "Priscila", "telefone": "3333-2221"}}

contatos.update({"priscila@gmail.com": {"nome": "Pri"}})
print(contatos)  # {'priscila@gmail.com': {'nome': 'Pri'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'priscila@gmail.com': {'nome': 'Pri'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)