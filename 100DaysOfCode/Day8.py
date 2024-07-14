import math
from resources.Day8_CaesarCipher.caesar_art import logo

def greet(fName, lName):
    print(f"Hello {fName} {lName}")
greet(lName="Modi", fName="Ashish")     # keyword argmts

def paint_calc(height, width, cover):
  nCanReqd = math.ceil((height * width) / cover)
  print(f"You'll need {nCanReqd} cans of paint.")

paint_calc(4, 9, 5)

def prime_checker(number):
  bIsPrime = True
  if number == 0 or number == 1:
    bIsPrime = False
  noDivBy2 = round(number / 2)
  for i in range(2, noDivBy2 + 1):  # +1 otherwise 4 will come as a prime no
    if number % i == 0:
      bIsPrime = False
  if bIsPrime:
    print("It's a prime number.")
  else:
    print("It's not a prime number.")

no = int(input("Enter the no to check for prime number: ")) # Check this number
prime_checker(number=no)

def caesar(sDirection, sMessage, nNoOfShifts):
  sFinalMsg = ""
  bEncode = sDirection == "encode"
  for char in sMessage:
    if char in arrAlphabets:
      chIndex = arrAlphabets.index(char)
      newIndex = chIndex + nNoOfShifts if bEncode == True else chIndex - nNoOfShifts
      if newIndex > len(arrAlphabets) - 1 or newIndex < 0:
        #newIndex = abs(newIndex - 25 - 1) if bEncode is True else (26 - abs(newIndex))
        newIndex = newIndex % 26 if bEncode is True else (26 - abs(newIndex))
      sFinalMsg += arrAlphabets[newIndex]
    else:
      sFinalMsg += char
  sFinalMsg = f"Encoded message is {sFinalMsg}" if bEncode is True else f"Decoded message is {sFinalMsg}"
  return sFinalMsg

arrAlphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
sTryAgain = "no"
bFirstRun = True

while sTryAgain == "yes" or bFirstRun is True:
  sDirection = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
  sMessage = input("Type your message: ").lower()
  nNoOfShifts = int(input("Type the shift number: ")) % 26
  sFinalPrint = caesar(sDirection, sMessage, nNoOfShifts)
  print(sFinalPrint)
  bFirstRun = False
  sTryAgain = input("Play with caesar cipher again?: ").lower()