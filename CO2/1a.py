def calc_factorial(x):
    if x==1:
        return 1
    else:
        return (x * calc_factorial(x-1))
num=int(input("Enter a NO:"))
print("Factorial of  ",num,"is",calc_factorial(num))