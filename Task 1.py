n = int(input("Enter a number: "))

def factorial(n):
    if n < 0:
        print("Factorial is not defined for negative numbers")
        return None
    
    r = 1 
    for t in range(1, n + 1):
        r = r * t
    return r

factorial(n)
if factorial(n) is not None:
    print(f"Factorial of {n} is: {factorial(n)}") 