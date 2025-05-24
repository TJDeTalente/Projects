x = input("Enter a sentence: ")
y = x.upper()
print(y)

w = input("Enter a paragraph")
word_count = len(w.split())
print(word_count)

f = input("Are these all digits?: ")
numbers_check = f.isdigit()
print(numbers_check)

o = input("Enter a sentence AND WATCH THE VOWELS!: ")
vowel_check = o.replace("a","o")
print(vowel_check)

name = input("Enter your full name please: ")
name_parts = name.split()
initials = ''.join(part[0].upper() for part in name_parts)
print(initials)

u = input("Enter a collection of words: ")
print(len(u))
