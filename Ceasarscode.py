alphabet = "ABCDEFGHIJKLMNOPRSTUWXYZABCDEFGHIJKLMNOPRSTUWXYZabcdefghijklmnoprstuwxyzabcdefghijklmnoprstuwxyzАБВГДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГДЕЄЖЗИІЇКЛМНОПРСТУФХЦЧШЩЬЮЯабвгдеєжзиіїклмнопрстуфхцчшщьюяабвгдеєжзиіїклмнопрстуфхцчшщьюя12345678901234567890"
a = input("Enter your text: ")
key = 1 
ins = ""
for letter in a:
    position = alphabet.find(letter)
    newPosition = position + key
    if letter in alphabet:
        ins = ins + alphabet[newPosition]
    else:
       ins = ins + letter
print("Encrypted text: ",ins)