linguas = {'br': 'portugues', 'eua':'ingles'}
print(type(linguas))
print(linguas)
print(linguas['br'])
print(linguas['eua'])
print(linguas.get('es'))
print(linguas.get('es', 'nao definida'))
print(linguas.get('br', 'nao definida'))
print('br'in linguas)
print('es' in linguas)
print(6 in list(range(10)))
print(11 in list(range(10)))
linguas['es'] = 'spanhol'
print(linguas['es'])

for chave in linguas:
    print(chave)

for chave in linguas.keys():
    print(chave)

for valor in linguas.values():
    print(valor)

for chave, valor in linguas.items():
    print(chave, valor)

print(linguas.pop('br'))
print(linguas)


