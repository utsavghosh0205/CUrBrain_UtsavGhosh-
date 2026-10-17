def divisible_prefix(arr, k):
    total = 0

    if k < 0:
        k = -k

    for i in range(len(arr)):
        total = total + arr[i]

        if total % k == 0:
            return True

    return False


print(divisible_prefix([4, 2, 9], 3))
print(divisible_prefix([1, 2, 4], 5))
print(divisible_prefix([5], 5))
print(divisible_prefix([0, 1], 7))
print(divisible_prefix([-2, 2, 1], 3))
