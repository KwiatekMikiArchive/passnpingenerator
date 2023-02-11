# No comments in english version...
import string, secrets, os
clearthis = lambda: os.system('cls, clear')

a = string.ascii_letters
b = string.digits
print("=====================")
print("𝚙𝚊𝚜𝚜𝚗𝚙𝚒𝚗𝚐𝚎𝚗")
print("=====================")

while True:
  c = input("What do you want to receive? [P̲(assword)/(P)i̲(n)/N̲(ick)]: ")

  if c in ["P", "p", "I", "i", "N", "n"]:
    break
  else:
    print("Invalid input. Please enter one of the following: P, p, I, i, N, n.")

if c in ["P", "p"]:
  while True:
    try:
      d = int(input("What length password do you need? [infinite range]: "))
      if d > 0:
        break
      else:
        print("Length must be a positive integer.")
    except ValueError:
      print("Length must be a positive integer.")
  e = ''.join(secrets.choice(a + b + string.punctuation) for i in range(d))
  clearthis()
  print("Your password is:")
  print(e)

if c in ["I", "i"]:
  while True:
    try:
      d = int(input("What length of PIN do you need? [infinite range]: "))
      if d > 0:
        break
      else:
        print("Length must be a positive integer.")
    except ValueError:
      print("Length must be a positive integer.")
  f = ''.join(secrets.choice(b) for i in range(d))
  clearthis()
  print("Your PIN is:")
  print(f)

if c in ["N", "n"]:
  print("Soon 👀")
