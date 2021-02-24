from statistics import mean

file = 'random_nums.txt'


def read_ints():
    data = []
    with open(file, 'r') as f:
        for num in f:
            num = int(num)
            data.append(num)

    return data


def count():
    total = 0
    data = read_ints()
    while total < len(data):
        total += 1

    return total


def summation():
    data = read_ints()
    sum = 0
    for x in range(len(data)):
        sum += x

    return sum


def average():
    return summation() / count()


def minimum():
    data = read_ints()
    min = data[0]
    for x in range(len(data)):
        if x < min:
            min = x
    return min


def maximum():
    data = read_ints()
    max = data[0]
    for x in range(len(data)):
        if x > max:
            max = x
    return max


def harmonic_mean():
    data = read_ints()
    n = count()
    numerator = 0
    for i in range(n):
        numerator += data[i] ** (-1)
    h_mean = (numerator / n) ** (-1)

    return h_mean


def variance():
    data = read_ints()
    n = count()
    numerator = 0
    mean_data = mean(data)
    for i in range(n):
        numerator += (data[i] - mean_data) ** 2
    var = numerator / n

    return var


def standard_dev():
    return variance() ** (1 / 2)


if __name__ == '__main__':
    print(read_ints())
    print(f'total = {count()}')
    print(f'summation = {summation()}')
    print(f'average = {average()}')
    print(f'Minimum = {minimum()}')
    print(f'Maximum = {maximum()}')
    print(f'Harmonic Mean = {harmonic_mean()}')
    print(f'Variance = {variance()}')
    print(f'Standard Deviation = {standard_dev()}')
