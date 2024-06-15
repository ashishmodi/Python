print("Hello"[4])       # starts with 0
print(12_3 + 456)       # underscore is just to make code readable
print("Type of len = " + str(type(len(input("What is your name?")))))  # <class 'int'>
print(70 + float("100.25"))  # 170.25
print(6 / 3)            # 2.0 always float with division
print(2 ** 3)           # exponent o/p 8
print(round(2.6666, 2)) # 2.67
print(8 // 3)           # 2 int instead of float

weight = float(input("Enter you weight in Kg: "))
height = float(input("Enter you height in Meters: "))   # 5.5 ft/ 3.281 = 1.67 meters
BMI = weight / height ** 2
print(f"Your BMI is {round(BMI)}\n")  # 2.6 -> 3 and 2.4 -> 2

age = int(input("Enter your age: "))
lifeLeft = (90 - age) * 52 
print(f"You have {lifeLeft} weeks left.")

fTotalBill = float(input("How much is the total bill? $"))
iNoOfPeople = int(input("How many no of people? "))
iTipPercentage = int(input("How much is the tip percentage? "))
fPerPersonBill = (fTotalBill + (fTotalBill * (iTipPercentage / 100))) / iNoOfPeople
fPerPersonBill = "{:.2f}".format(fPerPersonBill)    # round(fPerPersonBill, 2)
print(f"Per person bill = ${fPerPersonBill}")