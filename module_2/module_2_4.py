numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

for i in range(len(numbers)):
    is_prime = True
    if numbers[i] > 1:
        if numbers[i] == 2:
            primes.append(numbers[i])
            continue

        for j in range(2, numbers[i]):
            if numbers[i] % j == 0:
                not_primes.append(numbers[i])
                is_prime = False
                break

        if is_prime:
            primes.append(numbers[i])

print('Primes: ', primes)
print('Not Primes: ', not_primes)
