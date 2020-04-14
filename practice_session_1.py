import keyword
import constant

print(keyword.kwlist)
print("Hello this is python")

# global=1
# File"<Interactive Input>", line 1
# global=1

# while c=10 is
#    count=10

# Learn about variables

book = 5
website = 'learning'
print(website)
counter = 100
miles = int(100.0)
print(counter + miles)
a, b, c, d = "alfabet", 3, 4, 2
print(a, b, c, d)
print(a)
print(b)
print(c)


# Learn about global

def f():
    p = 50

    def g():
        global p
        p = 40

    print("Before calling g" + str(p))
    print("calling g now ")
    g()
    print("After calling g: " + str(p))


f()
print("p in main " + str(p))

x = "global"


def q():
    global x
    y = "Local"
    x = x * 2
    print(x)
    print(y)


q()

# Learn about constants

# PI = 3.14
# GRAVITY = 9.8
# print(constant.PI)
# print(constant.GRAVITY)
