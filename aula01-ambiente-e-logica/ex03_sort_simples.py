entrada = input().split()
originais = []

for i in entrada:
    originais.append(int(i))

originais_ordem = sorted(originais)

for i in originais_ordem:
    print(i)

print()
for i in originais:
    print(i)