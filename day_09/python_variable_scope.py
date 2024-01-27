##n Python, we can declare variables in three different scopes: local scope, global, and nonlocal scope. A variable scope specifies the region where we can access a variable. 

# outside function 
def outer():
    message = 'local'

    # nested function  
    def inner():

        # declare nonlocal variable
        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()

# outside function



#in this example, we have defined a variable message in the outer() function. Then, we have defined a nested function inner() and a nonlocal variable message inside it. This means that the variable message is not local to the inner() function. However, it is also not global. Therefore, when we change the value of the nonlocal variable message, the changes are reflected in the local variable as well.
