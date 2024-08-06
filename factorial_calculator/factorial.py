# Factorial Calculation: Implement a function to calculate the factorial of a number using both iterative and recursive approaches.

# iterative
def iterative_factorial(n):
    output = 0
    if n < 0:
        return "You cannot calculate the factorial of a negative number"
        
    
    if n == 0:
        output = 1
    else:
        output = 1
        for i in range(1, n + 1):
            output *= i
        
        
    return f"The factorial is: {output}" 
        
def recursive_factorial(n):
    if n < 0:
        return
    
    if n == 0 or n == 1:
        return 1
    else:
        return n * recursive_factorial(n - 1)

print(recursive_factorial(5))  # Should print 120
print(recursive_factorial(0))  # Should print 1
print(recursive_factorial(1))  # Should print 1
print(recursive_factorial(-3)) # Should print an error message
print(recursive_factorial(10)) # Should print 3628800
