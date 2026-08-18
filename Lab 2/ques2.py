import numpy as np

X=np.array([[10,100,5],
            [12,110,6],
            [11,105,7],
            [13,500,6],
            [14,108,8],
            [15,115,9]])

mean=np.mean(X,axis=0)
std=np.std(X,axis=0)
print("Mean:",mean)
print("Standard deviation:",std)
outlier=np.abs(X-mean)>2*std
print("Outlier matrix:")
print(outlier)
median=np.median(X,axis=0)
print("Column medians:",median)
result=np.where(outlier,median,X)
print("Result:")
print(result)