# No comments in english version...
import string, secrets, os
clearthis = lambda: os.system('clear')

a = string.ascii_letters
b = string.digits

c = input("What do you want to receive? [P(assword)/P(in)/N(ick)]: ")

if c == "P" or c == "p":
  d = input("What length password do you need? [infinite range]: ")
  e = ''.join(secrets.choice (a) for i in range(int(d)))
  clearthis()
  print("Your password is:")
  print(e)

if c == "P" or c == "p":
  d = input("What length of PIN do you need? [infinite range]: ")
  f = ''.join(secrets.choice (b) for i in range(int(d)))
  clearthis()
  print("Your PIN is:")
  print(f)

if c == "N" or c == "n":
  print("Soon 👀")