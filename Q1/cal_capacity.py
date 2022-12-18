import math
import numpy as np

# 隣接行列の定義
A = np.zeros((9,9))
A[0][1]=1
A[0][3]=1
A[0][5]=1
A[0][7]=1
A[1][2]=1
A[1][3]=1
A[1][5]=1
A[1][7]=1
A[2][3]=1
A[2][5]=1
A[2][7]=1
A[3][1]=1
A[3][4]=1
A[3][5]=1
A[3][7]=1
A[4][1]=1
A[4][5]=1
A[4][7]=1
A[5][1]=1
A[5][3]=1
A[5][6]=1
A[5][7]=1
A[6][1]=1
A[6][3]=1
A[6][7]=1
A[7][1]=1
A[7][3]=1
A[7][5]=1
A[7][8]=1
A[8][1]=1
A[8][3]=1
A[8][5]=1
print(A)

# 固有値取得
A_eig = np.linalg.eig(A)[0]
print(A_eig)

# 最大固有値
max_v = 0
for a_eig in A_eig:
    if max_v < abs(a_eig):
        max_v = abs(a_eig)
print(max_v)

# キャパシティ計算
print(math.log(max_v, 4))
