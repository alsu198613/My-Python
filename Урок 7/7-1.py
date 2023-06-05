class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join('\t'.join([f"{i:03}" for i in line]) for line in self.data)

    def __add__(self, other):
        try:
            m = [[int(self.data[line][itm]) + int(other.data[line][itm]) for itm in range(len(self.data[line]))]
                 for line in range(len(self.data))]
            return Matrix(m)
        except IndexError:
            return f'Матрицы имеют разный размер'


m_1 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
m_2 = [[2, 8, 21], [1, 5, 45], [3, 33, -9]]

mtrx_1 = Matrix(m_1)
mtrx_2 = Matrix(m_2)
new_m = mtrx_1 + mtrx_2
print(new_m)