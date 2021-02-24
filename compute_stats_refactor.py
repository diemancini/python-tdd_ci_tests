import os


class ComputeStatsRefactor:

    def __init__(self):
        self.file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "random_nums.txt")

    def read_ints(self):
        data = []
        with open(self.file, 'r') as f:
            for num in f:
                num = int(num)
                data.append(num)

        return data

    def count(self):
        total = 0
        data = self.read_ints()
        while total < len(data):
            total += 1

        return total

    def summation(self):
        data = self.read_ints()
        sum = 0
        for x in range(len(data)):
            sum += x

        return sum

    def average(self):
        return int(self.summation() / self.count())

    def minimum(self):
        data = self.read_ints()
        min = data[0]
        for x in range(len(data)):
            if x < min:
                min = x

        return min

    def maximum(self):
        data = self.read_ints()
        max = data[0]
        for x in range(len(data)):
            if x > max:
                max = x

        return max

    def harmonic_mean(self):
        data = self.read_ints()
        n = self.count()
        numerator = 0
        for i in range(n):
            numerator += data[i] ** (-1)
        h_mean = (numerator / n) ** (-1)

        return int(h_mean)

    def variance(self):
        data = self.read_ints()
        n = self.count()
        numerator = 0
        mean_data = self.average()
        for i in range(n):
            numerator += (data[i] - mean_data) ** 2
        var = numerator / n

        return int(var)

    def standard_dev(self):
        return int(self.variance() ** (1 / 2))


# if __name__ == '__main__':
#     csr = ComputeStatsRefactor()
#     # print(read_ints())
#     print(f'total = {csr.count()}')
#     print(f'summation = {csr.summation()}')
#     print(f'average = {csr.average()}')
#     print(f'Minimum = {csr.minimum()}')
#     print(f'Maximum = {csr.maximum()}')
#     print(f'Harmonic Mean = {csr.harmonic_mean()}')
#     print(f'Variance = {csr.variance()}')
#     print(f'Standard Deviation = {csr.standard_dev()}')
