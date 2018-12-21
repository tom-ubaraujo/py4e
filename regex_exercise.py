import re

big_list = []
int_list = []
total = 0

arq = open('regex_sum_143174.txt')
for line in arq:
    line = line.rstrip()
    lst = re.findall('[0-9]+',line)
    if lst != []:
        for l in lst:
            int_list.append(int(l))
            big_list.append(int_list)

for li in big_list[0]:
    total += li

print("Total de valores encontrados: {total}")
print("teste")