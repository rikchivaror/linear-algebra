from matrix import Matrix

# test case 1
A = Matrix([[3, 25, 9, 2, 4],
            [7, 15, 6, 92, 17],
            [31, 18, 0, 11, 8]])
A_t = Matrix([[3, 7, 31],
              [25, 15, 18],
              [9, 6, 0],
              [2, 92, 11],
              [4, 17, 8]])
ANS = A.transpose()
print(ANS)

if not A_t == ANS:
    print('test case 1 failed\n')
else:
    print('test case 1 passed\n')

# test case 2
A = Matrix([[5, 4, 1, 7],
            [2, 1, 3, 5]])
A_t = Matrix([[5, 2],
              [4, 1],
              [1, 3],
              [7, 5]])
ANS = A.transpose()
print(ANS)

if not A_t == ANS:
    print('test case 2 failed\n')
else:
    print('test case 2 passed\n')

# test case 3
A = Matrix([[5]])
A_t = Matrix([[5]])
ANS = A.transpose()
print(ANS)

if not A_t == ANS:
    print('test case 3 failed\n')
else:
    print('test case 3 passed\n')

# test case 4
A = Matrix([[5, 3, 2],
            [7, 1, 4],
            [1, 1, 2],
            [8, 9, 1]])
A_t = Matrix([[5, 7, 1, 8],
              [3, 1, 1, 9],
              [2, 4, 2, 1]])
ANS = A.transpose()
print(ANS)

if not A_t == ANS:
    print('test case 4 failed\n')
else:
    print('test case 4 passed\n')
