from matrix import Matrix

# test case 1
A = Matrix([[17, 25, 6, 2],
            [6, 1, 97, 4],
            [80, 8, 54, 15]])
B = Matrix([[3, 14, 1, 7, 42, 5],
            [32, 11, 2, 4, 18, 17],
            [19, 81, 4, 8, 5, 10],
            [27, 2, 3, 6, 7, 3]])
ANS = A.matrix_mult(B)
print(ANS)
if not ANS == Matrix([[1019, 1003, 97, 279, 1208, 576],
                      [2001, 7960, 408, 846, 783, 1029],
                      [1927, 5612, 357, 1114, 3879, 1121]]):
    print('test case 1 failed\n')
else:
    print('test case 1 passed\n')

# test case 2
A = Matrix([[5], [2]])
B = Matrix([[5, 1]])
ANS = A.matrix_mult(B)
print(ANS)
if not ANS == Matrix([[25, 5], [10, 2]]):
    print('test case 2 failed\n')
else:
    print('test case 2 passed\n')

# test case 3
A = Matrix([[5, 1]])
B = Matrix([[5], [2]])
ANS = A.matrix_mult(B)
print(ANS)
if not ANS == Matrix([[27]]):
    print('test case 3 failed\n')
else:
    print('test case 3 passed\n')

# test case 4
A = Matrix([[4]])
B = Matrix([[3]])
ANS = A.matrix_mult(B)
print(ANS)
if not ANS == Matrix([[12]]):
    print('test case 4 failed\n')
else:
    print('test case 4 passed\n')

# test case 5
A = Matrix([[2, 1, 8, 2, 1],
            [5, 6, 4, 2, 1]])
B = Matrix([[1, 7, 2],
            [2, 6, 3],
            [3, 1, 1],
            [1, 20, 1],
            [7, 4, 16]])
ANS = A.matrix_mult(B)
print(ANS)
if not ANS == Matrix([[37, 72, 33],
                      [38, 119, 50]]):
    print('test case 5 failed\n')
else:
    print('test case 5 passed\n')
