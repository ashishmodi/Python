a = 15
print(not a < 14)

weight = float(input("Enter you weight in Kg: "))
height = float(input("Enter you height in Meters: "))   # 5.5 ft/ 3.281 = 1.67 meters👇
fBmi = weight / height ** 2     # no round is needed
if fBmi < 18.5:
  print(f"Your BMI is {fBmi}, you are underweight.")
elif fBmi >= 18.5 and fBmi < 25:    # no and condition is needed
  print(f"Your BMI is {fBmi}, you have a normal weight.")
elif fBmi >= 25 and fBmi < 30:
  print(f"Your BMI is {fBmi}, you are slightly overweight.")
elif fBmi >= 30 and fBmi < 35:
  print(f"Your BMI is {fBmi}, you are obese.")
else:
  print(f"Your BMI is {fBmi}, you are clinically obese.")

year = int(input("Enter the year for the leap year check: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  print("Leap year")
else:
  print("Not leap year")

name1 = input("What is your name?")
name2 = input("What is their name?")

sCombinedName = name1 + name2
sCombinedName = sCombinedName.lower()
nTrueCount = 0
nTrueCount += sCombinedName.count("t")
nTrueCount += sCombinedName.count("r")
nTrueCount += sCombinedName.count("u")
nTrueCount += sCombinedName.count("e")
nLoveCount = 0
nLoveCount += sCombinedName.count("l")
nLoveCount += sCombinedName.count("o")
nLoveCount += sCombinedName.count("v")
nLoveCount += sCombinedName.count("e")

nTotalScore = int(str(nTrueCount) + str(nLoveCount))
if nTotalScore < 10 or nTotalScore > 90:
  print(f"Your love score is {nTotalScore}, you go together like coke and mentos.")
else:
  print(f"Your love score is {nTotalScore}.")