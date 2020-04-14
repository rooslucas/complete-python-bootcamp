import keyword
import tryouts

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

PI = 3.14
GRAVITY = 9.8
print(tryouts.PI)
print(tryouts.GRAVITY)

# Learn about Statements/Comments
print("This is useful to understand your program")

# Learn about Type Convention
# Implicit

num_int = 1333
num_float = 1.25
num_new = num_int + num_float

print("Data type of int Num ", type(num_int))
print("Data type of float Num ", type(num_float))

print("Value of num new ", num_new)
print("Data type of num new ", type(num_new))

# Explicit
num_int2 = 1333
num_str = "856"

print("Data type of int Num ", type(num_int))
print("Data type of string Num ", type(num_str))
num_str = int(num_str)
print("Data type of num str after type cating ", type(num_str))
num_sum = num_int2 + num_str

print("Sum of num int and num str ", num_sum)
print("Data type of the sum ", type(num_sum))


