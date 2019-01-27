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

# test case 6
A = Matrix([[5, 3, 1],
            [6, 2, 7]])
B = Matrix([[4, 2],
            [8, 1],
            [7, 4]])
ANS = Matrix([[51, 17],
              [89, 42]])
RESULT = A.matrix_mult(B)
print(RESULT)
if not ANS == RESULT:
    print('test case 6 failed\n')
else:
    print('test case 6 passed\n')

# test case 7
A = Matrix([[5]])
B = Matrix([[4]])
ANS = Matrix([[20]])
RESULT = A.matrix_mult(B)
print(RESULT)
if not ANS == RESULT:
    print('test case 7 failed\n')
else:
    print('test case 7 passed\n')

# test case 8
A = Matrix([[2, 8, 1, 2, 9],
            [7, 9, 1, 10, 5],
            [8, 4, 11, 98, 2],
            [5, 5, 4, 4, 1]])
B = Matrix([[4],
            [2],
            [17],
            [80],
            [2]])
ANS = Matrix([[219], [873], [8071], [420]])
RESULT = A.matrix_mult(B)
print(RESULT)
if not ANS == RESULT:
    print('test case 8 failed\n')
else:
    print('test case 8 passed\n')

# test case 9
A = Matrix([[2, 8, 1, 2, 9],
            [7, 9, 1, 10, 5],
            [8, 4, 11, 98, 2],
            [5, 5, 4, 4, 1]])
B = Matrix([[4, 1, 2],
            [2, 3, 1],
            [17, 8, 1],
            [1, 3, 0],
            [2, 1, 4]])
ANS = Matrix([[61, 49, 49],
              [83, 77, 44],
              [329, 404, 39],
              [104, 65, 23]])
RESULT = A.matrix_mult(B)
print(RESULT)
if not ANS == RESULT:
    print('test case 9 failed\n')
else:
    print('test case 9 passed\n')
