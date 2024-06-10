# i = 0
# # break loop
# while i < 5:
#     if i == 3:
#         break
#     print(i)
#     i += 1

# i = 0 
# # continue loop
# while i < 5: 
#     i += 1
#     if i == 3: 
#         continue
#     print(i)

# # skipping vowels from a text
# text = "coder academy"
# vowels = "aeiouAEIOU"

# for each in text:
#     if each in vowels:
#         continue
#     print(each, end="")


# Stop when there is 'stop'
signals = ["start", "halt", "continue", "start", "stop", "hold"]

for each in signals: 
    if each == "stop":
        break
    print(each)



