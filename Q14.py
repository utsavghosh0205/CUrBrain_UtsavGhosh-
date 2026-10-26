sales = [150, 80, 200, 90, 300]
threshold = 100

result = []

for i in range(len(sales)):
    if (sales[i] >= threshold):
        result.append(sales[i])

print(result)
