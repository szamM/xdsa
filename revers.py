def revers(list_of_data):
    for i in range(len(list_of_data) // 2):
        print(i)
        list_of_data[i], list_of_data[-i - 1] = list_of_data[-i - 1], list_of_data[i]
    return list_of_data


print(revers([1, 2, 3, 4, 5, 6, 7]))