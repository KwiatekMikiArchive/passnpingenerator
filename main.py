# No comments in english version...
import string, secrets, os
clearthis = lambda: os.system('cls, clear')
a = string.ascii_letters
b = string.digits
f = special_characters + a + b

print("=====================")
print("𝚙𝚊𝚜𝚜𝚗𝚙𝚒𝚗𝚐𝚎𝚗")
print("=====================")

c = input("What do you want to receive? [P̲(assword)/(P)i̲(n)/N̲(ick)]: ")

if c == "P" or c == "p":
  d = input("What length password do you need? [infinite range]: ")
  e = ''.join(secrets.choice (f) for i in range(int(d)))
  clearthis()
  print("Your password is:")
  print(e)

if c == "I" or c == "i":
  d = input("What length of PIN do you need? [infinite range]: ")
  e = ''.join(secrets.choice (f) for i in range(int(d)))
  clearthis()
  print("Your PIN is:")
  print(f)

if c == "N" or c == "n":
  print("Soon 👀")
