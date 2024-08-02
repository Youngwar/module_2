


def password():
    combination = []
    x = int(input ('Введите необходимое число: '))
    i = 0
    for k in range(1, x):
        for j in range(1, x):
            if k==j:
                continue
            elif [j, k] in combination:
                continue

            elif x % (k+j) == 0:
                combination.append([])
                combination[i].append(k)
                combination[i].append(j)
                i += 1
    return combination

password = str(password())
password = password.replace("[", '')
password = password.replace("]", '')
password = password.replace(", ", '')
print(password)
