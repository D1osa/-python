class Matrix:

    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        list_of_lists = []
        for i in a:
            list_of_lists.append([j for j in i])
        self.a = list_of_lists

    def __str__(self):
        self.c = str(self.a)
        return self.c

    def __add__(self, other):
        result = []
        numbers = []
        for i in range(len(self.a)):
            for j in range(len(self.a[0])):
                sum_mat = other.a[i][j] + self.a[i][j]
                numbers.append(sum_mat)
                if len(numbers) == len(self.a):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m_2 = Matrix([[3, 2, 1], [6, 5, 4], [9, 8, 7]])
print(m_1 + m_2)
