notas = [0,10.0,7.0,8.0]
notas_2 = [7.0,8.0,9.0,6.0]

uniao_notas = notas
for elemento in notas_2:
    if elemento not in notas:
        uniao_notas.append(elemento)

print(sorted(uniao_notas))
# uniao_notas.extend(elemento for elemento in notas_2 if elemento not in notas)
# print(sorted(uniao_notas))
#
# print('A soma das notas:', sum(notas))
#
# notas.insert(1,5.0)
#
# print(notas)
#
#
#
#
# animais = ['gato','cachorro','papagaio','axolote']
#
# print(max(animais))
# print(min(animais))
#
#
# animais.remove('gato')
#
# print(animais)
#
# exemplo = ['z', 'y'] + ['x']
#
# print(exemplo)
#
# exemplo += [3,]
# print(exemplo)
# exemplo = exemplo * 2
# print(exemplo)