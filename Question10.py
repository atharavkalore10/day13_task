import numpy as np

try:
    n = int(input("How many numbers do you want to generate? "))

    arr = np.random.randint(10,101,n)

    print("\nGenerated Array")
    print(arr)

    print("\nMean:", np.mean(arr))

    print("Median:", np.median(arr))

    print("Standard Deviation:", np.std(arr))

    print("Minimum:", np.min(arr))

    print("Maximum:", np.max(arr))

    if n % 2 == 0:
        matrix = arr.reshape(2, n//2)

        print("\nReshaped Array")

        print(matrix)

        print("\nRow-wise Sum")

        print(np.sum(matrix, axis=1))

    else:
        print("\nCannot reshape into a 2D array because the number of elements is odd.")

except ValueError:
    print("Please enter a valid integer.")
except Exception as e:
    print("Error:", e)