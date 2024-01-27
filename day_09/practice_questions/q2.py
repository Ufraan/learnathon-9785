#Write a recursive function to reverse a string.



def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

text = "Hello, World!"
result = reverse_string(text)
print(f"The reversed string is: {result}")

