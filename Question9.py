import numpy as np

arr = np.random.randint(1,51,20)

matrix = arr.reshape(4,5)

print(matrix)

print("Sum:", matrix.sum())

print("Mean:", matrix.mean())

print("Standard Deviation:", matrix.std())

print("Maximum in each row")

print(matrix.max(axis=1))