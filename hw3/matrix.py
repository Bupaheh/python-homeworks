class MatrixHashMixin:
    """Sum of matrix elements"""
    def __hash__(self):
        h = 0
        for row in self._m:
            for elem in row:
                h += elem
        return h

    def __eq__(self, other):
        if not isinstance(other, Matrix):
            return False

        return self._m == other._m


class Matrix(MatrixHashMixin):
    _cache = {}

    def __init__(self, m):
        if not isinstance(m, list) or any([not isinstance(row, list) for row in m]):
            raise ValueError('Invalid matrix')

        self._m = m
        self.rows = len(m)
        self.cols = len(m[0])

        for row in m:
            if len(row) != self.cols:
                raise ValueError('Invalid matrix')

    def __add__(self, other):
        if not isinstance(other, Matrix) or other.rows != self.rows or other.cols != self.cols:
            raise ValueError('Invalid argument')

        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self._m[i][j] + other._m[i][j])
            result.append(row)

        return Matrix(result)

    def __mul__(self, other):
        if not isinstance(other, Matrix) or other.rows != self.rows or other.cols != self.cols:
            raise ValueError('Invalid argument')

        result = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self._m[i][j] * other._m[i][j])
            result.append(row)

        return Matrix(result)

    def __matmul__(self, other):
        if not isinstance(other, Matrix) or self.cols != other.rows:
            raise ValueError('Invalid argument')

        cached = Matrix._cache.get((hash(self), hash(other)))
        if cached is not None:
            return cached

        result = []
        for i in range(self.rows):
            row = []
            for j in range(other.cols):
                el = 0
                for k in range(self.cols):
                    el += self._m[i][k] * other._m[k][j]
                row.append(el)
            result.append(row)

        result = Matrix(result)
        Matrix._cache[(hash(self), hash(other))] = result
        return result

    def __str__(self):
        res = ""
        for row in self._m:
            for el in row:
                res += "{:5d}".format(el)
            res += "\n"

        if len(res) > 0:
            return res[:-1]
        else:
            return res
