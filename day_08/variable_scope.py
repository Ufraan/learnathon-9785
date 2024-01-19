#A variable scope specifies the region where we can access a variable.



def outer():
    message = 'local'

    def inner():

        nonlocal message

        message = 'nonlocal'
        print("inner:", message)

    inner()
    print("outer:", message)

outer()