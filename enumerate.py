animals = ["cat", "dog", "bird", "rabbit"]

for index, animal in enumerate(animals):
    print(f"{index}: {animal}")



fruits = ["apple", "banana", "cherry", "dates"]

target = "cherry"

for index, fruit in enumerate(fruits):
    if fruit == target:
        print(f"found '{target}' at {index}")