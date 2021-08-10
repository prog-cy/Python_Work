word = input("Enter string: ")

finalWord = ''

for letter in word:
  if letter.isupper():
    finalWord += letter.lower()
  elif letter.islower():
    finalWord += letter.upper()

print("Final word is: "+finalWord)