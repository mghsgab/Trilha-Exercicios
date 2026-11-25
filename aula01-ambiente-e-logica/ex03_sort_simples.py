entrada = input().split()
originais =[]

for i in entrada:
    originais.append(int(i))

originais_ordem = sorted(originais)

for i in range(min(3, len(originais))):
    print(originais_ordem[i])

print('/n')

for i in range(min(3,len(originais))):
    print(originais[i])