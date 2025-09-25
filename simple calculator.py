def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "awa chdakay kaka atw"
    return a/b
while True:
    print("\n" + "=" * 30)
    try:
        num1 = float(input("zhmarai yakam: "))
        operator = input("(+, -, *, /): ")
        num2 = float(input("zhmarai dwam: "))
        
        if operator == '+':
            dabta = add(num1, num2)
        elif operator == '-':
            dabta = subtract(num1, num2)
        elif operator == '*':
            dabta = multiply(num1, num2)
        elif operator == '/':
            dabta = divide(num1, num2)
        else:
            print("hemaka halaya")
            continue
        
        print(f"Dabta: {dabta}")
    except ValueError:
        print("halaya")
    except KeyboardInterrupt:
        print("\nbye bye")
        break
