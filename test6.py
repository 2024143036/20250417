def add(a,b):
    return a+b

print(add(3,5))

c=add(4,8)
print(c)

def add_and_mul(a,b):
    return [a+b,a*b]

print(add_and_mul(3,6))
c,d=add_and_mul(4,10)
print(c)

# def say_hello():
#     result=0
#     for j in args:
#         result+=j
#     return result
# say_hello()

def add_many(*args):
    result=0
    for j in args:
        result+=j
    return result

print(add_many(1,2,3,4,5,6))




