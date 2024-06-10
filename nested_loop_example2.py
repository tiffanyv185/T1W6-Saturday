# initialise a variable
string_list =["Coder", "Academy", "Champion"]
result = 0

for string in string_list:
    for letter in string:
        if letter in "AEIOUaeiou":
            result += 1
        
print("the total occurence of vowels is:", result)