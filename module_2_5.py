def get_matrix():
    n = input('Введите количество строк: ', )
    m = input('Введите количество столбцов: ', )
    value = input('Введите значение: ', )
    matrix = []
    for i in range(int(n)):
        matrix.append([])

        for k in range(int(m)):
            matrix[i].append(value)
            continue


    return matrix
print(get_matrix())

