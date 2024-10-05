
N = int(input('Кол-во участников: '))
members = []
num = 1
for _ in range(N // 3):
    members.append(list(range(num, num + 3)))
    num +=3

print(members)

for i in members:
    print(i)

for i_team in members:
    for i_man in i_team:
        print(i_man, end=' ')
    print()

