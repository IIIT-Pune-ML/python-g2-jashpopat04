import numpy as np

P=np.array([[1,2],
            [4,6],
            [7,3],
            [2,8],
            [9,5]])

diff=P[:,np.newaxis,:]-P[np.newaxis,:,:]
D=np.sqrt(np.sum(diff**2,axis=2))

print("Distance Matrix:")
print(D)

max_index=np.unravel_index(np.argmax(D),D.shape)

print("Maximum distance:",D[max_index])
print("Pair of points:",max_index)