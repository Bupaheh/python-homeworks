from matrix import Matrix
import numpy as np

if __name__ == '__main__':
    a = Matrix([[1, 2]])
    c = Matrix([[3, 0]])
    b = Matrix([[4], [0]])
    d = Matrix([[4], [0]])

    assert hash(a) == hash(c)
    assert a != c
    assert b == d
