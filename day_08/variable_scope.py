#A variable scope specifies the region where we can access a variable.  There are two types of variable scopes in Python:



def outer():
    message = 'local'

    def inner():

        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()