# tuple fron iterobj
L = [1, 2, 3]
iterator = iter(L)
t = tuple(iterator)
print(t)

# genexps and listcomps
"""
Generator expressions are surrounded by parentheses (“()”)and list comprehensions are surrounded by square brackets (“[]”)
"""
xs = [4, 6, 7, 9, 10]
xss = (x * 2 for x in xs)
print(xss) # xss is an iterobj

xss_list = [x*2 for x in xs]
print(xss_list) # xss_list is a list

# Generator functions and yields

def agen():
    i = 10
    yield [i, i, i]

a, b, c = agen()
