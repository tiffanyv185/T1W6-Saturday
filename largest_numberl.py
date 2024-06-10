numbers = [1, 55, 22, 28, 93, 11, 33, 36, 32, 88, 9262]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(largest)

