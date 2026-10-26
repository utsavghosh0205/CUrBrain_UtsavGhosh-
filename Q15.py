arr = [10, -5, -2, 4, 2]

smallest = arr[0]

for i in range(1, len(arr)):
    if abs(arr[i]) < abs(smallest):
        smallest = arr[i]

print(smallest)
