#Write a Python program that defines a function called outer_function. Inside outer_function, declare a variable x with a value of 10. Then, define another function called inner_function inside outer_function. Inside inner_function, declare a variable y with a value of 5. Return the sum of x and y from inner_function. Finally, call outer_function and print the result.


def outer_function():
    x = 10  
    
    def inner_function():
        y = 5 
        return x + y  
    
    result = inner_function()
    return result

result_value = outer_function()
print("result is =  {result_value}")