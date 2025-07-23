def fact(n):
    result=1
    for i in range(2, n+1):
        result=result*i
    return result
n=int(input("Enter a number to generate its factorial: "))
print(fact(n))