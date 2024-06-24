import random
nRandomNo = random.randint(1, 15)   # range including a and b
fRandomNo = random.random()         # 0.0000 to 0.9999
print(f"{nRandomNo}, {fRandomNo}, Random no = {nRandomNo + fRandomNo}")

lsStatesOfIndia = ["Maharashtra", "Arunachal Pradesh", "Madhya Pradesh"]
lsStatesOfIndia.append("Chennai")
lsStatesOfIndia.extend(["Tripura", "Meghalaya"])
print(f"{lsStatesOfIndia[-1]}, Total states = {len(lsStatesOfIndia)}")  # prints from backwards
# lsStatesOfIndia = lsStatesOfIndia.split(" ")

fruits = ["Mango", "Strawberries", "Peach"]
vegetables = ["Potato", "Spinach", "Celery"]
dirty_dozens = [fruits, vegetables]
print(dirty_dozens[1][2])       # Celery

line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input("Where do you want to put the treasure?")

column = position[0]
row = position[1]
if column == "A":
  if row == "1":
    line1[0] = "X"
  elif row == "2":
    line2[0] = "X"
  else:
    line3[0] = "X"
elif column == "B":
  if row == "1":
    line1[1] = "X"
  elif row == "2":
    line2[1] = "X"
  else:
    line3[1] = "X"
elif column == "C":
  if row == "1":
    line1[2] = "X"
  elif row == "2":
    line2[2] = "X"
  else:
    line3[2] = "X"  
print(f"{line1}\n{line2}\n{line3}")

print("With optimized solution:")
letter = position[0]
ABC = ["A", "B", "C"]
letterIndex = ABC.index(letter)
arrayNumberIndex = int(position[1]) - 1;
map[arrayNumberIndex][letterIndex] = "X"
print(f"{line1}\n{line2}\n{line3}")

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

lsGameImages = [rock, paper, scissors]

nUserChoice = int(input("Type 0 for Rock, 1 for Paper, 2 for Scissor: "))
print(lsGameImages[nUserChoice])
nComputerChoice = random.randint(0, 2)
print(f"Computer selected: {nComputerChoice}")
print(lsGameImages[nComputerChoice])
bUserWins = True
if (nUserChoice == 0 and nComputerChoice == 1) or (nUserChoice == 1 and nComputerChoice == 2) or (nUserChoice == 2 and nComputerChoice == 0):
  bUserWins = False
elif nUserChoice == nComputerChoice:
  print("This is draw!")
print(f"User won? {bUserWins}")