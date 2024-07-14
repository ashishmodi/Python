arrAlphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

index = arrAlphabets.index('x')
shift = 5
newIndex = index + shift
temp = 25 - index   # 2
pendingShift = shift - temp
print(f"{index} {arrAlphabets[index]}")