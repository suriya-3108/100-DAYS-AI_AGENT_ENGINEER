# Getting Input from user

user_input = input("Enter a paragraph: ")
print("\n")
# Printing Original Text

print(f"Original Text:\n{user_input}\n")

"""PHASE 1 — Text Cleaning
Processing:

1) Convert to lowercase
2) Remove punctuation
3) Remove extra spaces
"""

lower_str = user_input.lower()

remove = []
punctuation = []

for i in lower_str:
    remove.append(i)

for val in remove:
    if val.isspace():
        punctuation.append(val)
    elif val.isalpha():
        punctuation.append(val)

punctuation_removed = ''.join(punctuation)

original_punctuation_removed = []
actaul_output = []

for b in punctuation_removed.strip():
    original_punctuation_removed.append(b)

for act in original_punctuation_removed:
    actaul_output.append(''.join(act))
    
res = ''.join(actaul_output)

print(f"Cleaned Text:\n{res}\n")


"""PHASE 2 — Word Analysis (Dictionary Core Phase)"""

s1 = []
s2 = ''

for org in actaul_output:
    s2 += org
    if org == ' ':
        s1.append(s2)
        s2 = ''
s1.append(s2)

freq = {}
total = 0
key_count = 0
max_used = []
min_used = []

for find in s1:
    freq[find] = freq.get(find, 0) + 1
    

for keys,values in freq.items():
    total += values
    key_count += 1
    if values > 1:
        max_used.append(keys)
    else:
        min_used.append(keys)
        
s1 = [word.strip() for word in s1 if word.strip() != ""]
    
s3 = []
s4 = []
for z in s1:
    if z not in s3:
        s3.append(z)
    else:
        s4.append(z)
s3.sort()


print(f"Total Words:{total}\n")

print(f"Key Count: {key_count}\n")

print("Word Frequency: ")
for f_keys,f_values in freq.items():
    print(f"{f_keys} -> {f_values}")
print("\n")
   
print(f"Most Frequent Word:",end=" ")
for high in max_used:
    print(f"{high}",end=" ")
print("\n")

print(f"Least Frequent Words:",end=" ")
for low in min_used:
    print(f"{low}",end=" ")
print("\n")

print(f"Alphabetical Order:")
for alp in s3:
    print(alp)
print("\n")


"""PHASE 3 — Character Analysis"""

counter = 0
vowel = 0
consonant = 0
letter_freq = ''
char_freq = {}
longest = float("-inf")
shortest = float("inf")
longest_word = ''
shortest_word = ''
check = ''
VOWELS = ['A','E','I','O','U','a','e','i','o','u']

for result in res:
    if result.isalpha(): 
        counter += 1   #count
    
        if result in VOWELS:
            vowel += 1
        else:
            consonant += 1
        
       
for word in s3:
    if len(word) > longest:
        longest_word = word
        longest = len(word)
    if len(word) < shortest:
        shortest_word = word 
        shortest = len(word)   
    for letter in word:
        char_freq[letter] = char_freq.get(letter, 0) + 1

print(f"Total Characters:{counter}")
print("\n")

print(f"Vowels:{vowel}")
print("\n")

print(f"Consonants:{consonant}")
print("\n")

print("Character Frequency:")
for char_keys, char_values in char_freq.items():
    print(f"{char_keys} -> {char_values}")
print("\n")

"""PHASE 4 — Advanced Insights (Interview Level)"""

print("Duplicate words: ")
for dup in s4:
    print(dup, end=" ")
print("\n")

print(f"Longest word:{longest_word}")
print("\n")

print(f"Shortest word:{shortest_word}")
print("\n")

for palindrome in res:
    if palindrome != ' ':
        check += palindrome

if check == check[::-1]:
    print(f"Is entire sentence palindrome? → yes")
else:
    print(f"Is entire sentence palindrome? → No")
    