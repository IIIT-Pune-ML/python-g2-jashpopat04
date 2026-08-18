import numpy as np

A=np.array([[12,5,8,20],
            [7,15,3,11],
            [25,9,18,6],
            [10,14,2,16]])

row_mean=np.mean(A,axis=1)
print("Row means:",row_mean)

B=(A>row_mean[:,np.newaxis]).astype(int)

print("Binary matrix:")
print(B)

count=np.sum(B,axis=1)
max_row=np.argmax(count)

print("Count of elements above mean:",count)
print("Row with maximum elements above mean:",max_row+1)