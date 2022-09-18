

phrase = input("Input: ")
vowels = "aeiouAEIOU"
x = 0
final_phrase = ""
for i in range(len(phrase)):
    for j in range(len(vowels)):
        if phrase[i] == vowels[j]:
            x = 1
    if x == 0:
        final_phrase = final_phrase + phrase[i]
    x = 0
print("Output:", final_phrase)