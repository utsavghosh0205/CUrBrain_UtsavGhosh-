def modular_addition(arr):
    MOD = 1000000007
    result = 0

    for i in range(len(arr)):
        result = (result + arr[i]) % MOD

    return result


print(modular_addition([1000000000, 1000000000, 1000000000]))
print(modular_addition([1, 2, 3, 4]))
print(modular_addition([]))
print(modular_addition([1000000007]))
print(modular_addition([0, 0, 0]))
