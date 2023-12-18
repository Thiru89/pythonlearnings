# Opertions : + - * /
# convesion order int -->float -->complex
# Integers can be converted to floats however, viceversa is not possible
x = 28 #int
y = 28.0 #float
# print(float(28))

z = 3.14 
# print(int(z))

# convert Float to complex. Floats can be converted to complex but viceversa is not possible
x = 1.732
# print(type(x+0j))

a = 2
b = 6.0
c =12 + 0j

# print(complex(b))
# print(complex(a))
# print(float(a))
# print("<---------below conversion will fail---------->")
# print(float(c))
# print(float(c))
# print(int(b))
# print(int(c))


print("Sum of a+b is ", (a+b) )
print("type of a+b is ", type(a+b))

print("Sum of b+c is ", (b+c) )
print("type of b+c is ", type(b+c))

print("Sum of a+c is ", (a+c) )
print("type of a+c is ", type(a+c))

print(16/5)
print(20/5)  # division
print(16%5)  # remaindar
print(16//5) # Quotient
