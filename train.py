"""
Comment
"""
print("Hello World")
if 5 > 2:
    print("5 is greater than 2")
x = 5
y = "sss"
z = float(35.2312)

print(str(z) + str(type(z)))


#array

fruits = ["apple", "Banana", "Cherry"]

x, y, z = fruits

print(x + "  "  + y+ "  " + z)

print(x, y, z)

z = 3.5

print(x ,z)

x = 3+5j
y = 5j
z = -5j

print(x)
print(type(y))
print(type(z))

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()