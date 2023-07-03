import secrets, ctypes
import json, os, locale

if not os.path.exists(f"./chars.txt"):
  raise FileNotFoundError("Can't find chars.txt. Did you run this in a correct folder?")

with open(f'chars.txt', 'r', encoding='utf-8') as f:
  chars = f.read()

# Check language and translate this code
windll = ctypes.windll.kernel32
oglang = locale.windows_locale[windll.GetUserDefaultUILanguage()] # With help of StackOverflow [https://stackoverflow.com/a/25691701] and ChatGPT!
oslang = oglang.split("_")[0]

if not os.path.exists(f"./lang"):
  raise FileNotFoundError("Can't find 'lang' folder. Did you run this in a correct folder?")

if not os.path.exists(f"./lang/{oslang}.json"):
  print("Can't find a translation for your Windows language, using English.")
  oslang = "en"

with open(f'./lang/{oslang}.json', 'r', encoding='utf-8') as f:
  trans = json.load(f)

menu = trans["menu"]
lets = trans["letters"]
passt = trans["password"]
pint = trans["pin"]
nickt = trans["nick"]

# Function to shorten the code
def strtoint(l):
  try:
    return int(l)
  except ValueError:
    raise ValueError(trans["notint"])
  except:
    raise TypeError("Something went wrong.")

def checklen(l, min, max):
  l = int(l)
  if l > max or l < min:
    raise ValueError(trans["wronglength"])

# Main
print("""
█▀█ ▄▀█ █▀ █▀ █▄ █ █▀█ █ █▄ █
█▀▀ █▀█ ▄█ ▄█ █ ▀█ █▀▀ █ █ ▀█
       by KwiatekMiki
""")

what = input(f"{menu['what']} [{menu['tip']}]: ").lower()

if what == lets["pass"]:
  length = input(f"{passt['howlong']} [4-100]: ")
  strtoint(length)
  checklen(length, 4, 100)
  
  passwd = ''.join(secrets.choice(chars) for i in range(int(length)))
  print(f"{passt['your']}: {passwd}")

elif what == lets["pin"]:
  length = strtoint(input(f"{passt['howlong']} [4-10]: "))
  checklen(length, 4, 10)
  
  if length > 10 or length < 4:
    raise ValueError(trans["wronglength"])
  
  pin = ''.join(secrets.choice("1234567890") for i in range(int(length)))
  print(f"{pint['your']}: {pin}")

elif what == lets["nick"]:
  print(nickt["soonTM"])