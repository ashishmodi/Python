import random

fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)

lsHeights = input("Enter space separted heights: ").split()     # takes space separted heights 10 30 50
for n in range(0, len(lsHeights)):      # excluding end i.e. includes o to len(lsHeights) - 1.
    lsHeights[n] = int(lsHeights[n])
nTotalHeight = 0
nCountStudents = 0
for height in lsHeights:
    nTotalHeight += height
    nCountStudents += 1
nAvgHeight = round(nTotalHeight/nCountStudents)
print(f"average height = {nAvgHeight}")

for no in range(1, 11, 3):      # 1 4 7 10
    print(no)

target = int(input("Enter a no between 0 and 1000 to calculate sum of even no's: "))
nSumEvenNos = 0
# optimized soln    for no in range(1, target + 1):   if no % 2 == 0:     nSumEvenNos += no
for no in range(2, target + 1, 2):
   nSumEvenNos += no

print(f"Sum of even no's between 1 to {target} = {nSumEvenNos}")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

strLetters = ""
for i in range(0, nr_letters):
    # strLetters += random.choice(letters)      # optimized
    no = random.randint(0, len(letters) - 1)
    strLetters += letters[no]

strNumbers = ""
for i in range(0, nr_numbers):
    no = random.randint(0, len(numbers) - 1)
    strNumbers += numbers[no]

strSymbols = ""
for i in range(0, nr_symbols):
    no = random.randint(0, len(symbols) - 1)
    strSymbols += symbols[no]

mergedStr = strLetters + strNumbers + strSymbols
print(f"Merged string = {mergedStr}")

sFinalPwd = ""
lsVisitedNo = []
# random.shuffle(mergedStr)     # Optimized solution
for i in range(0, len(mergedStr)):
    randomNo = random.randint(0, len(mergedStr) - 1)
    if lsVisitedNo.count(randomNo) == 0:
        lsVisitedNo.append(randomNo)
    else:
        while lsVisitedNo.count(randomNo) == 1:
            randomNo = random.randint(0, len(mergedStr) - 1)
            if lsVisitedNo.count(randomNo) == 0:
                lsVisitedNo.append(randomNo)
                break
    
    sFinalPwd += mergedStr[randomNo]

print(f"Your password is: {sFinalPwd}")