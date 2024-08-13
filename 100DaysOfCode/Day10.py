def outer_fun(a, b):
    """Demo of inner fn"""
    def inner_fun(a, b):
        return a / b
    return inner_fun(a, b)
result = outer_fun(10, 20)
print(f"10/20 = {result}")

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1, n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
dictFn = {"+": add, "-": sub, "*": mul, "/": div}
n1 = float(input("Please enter your first no: "))
n2 = float(input("Please enter your second no: "))
sUserOp = input("Enter the operation you wish to perform: ")
nOldOutput = dictFn[sUserOp](n1, n2)
print(f"Output of {n1} {sUserOp} {n2} is: {nOldOutput}")
bContinue = True
sAnotherOp = input(f"Do you want to perform another operation on {nOldOutput}? ")
while(sAnotherOp == "yes"):
    nNewNo = float(input("Please another no: "))
    sUserOp = input("Enter the operation you wish to perform: ")
    nFinalOutput = dictFn[sUserOp](nOldOutput, nNewNo)
    print(f"Output of {nOldOutput} {sUserOp} {nNewNo} is: {nFinalOutput}")
    sAnotherOp = input(f"Do you want to accumulate another operation on {nFinalOutput}? ")
    nOldOutput = nFinalOutput if sAnotherOp == "yes" else nOldOutput