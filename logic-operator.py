x = 10
y = 20
z = 30
print(x > y and y > z)
if x > y and y > z:
    print("x is the largest number.")
else:
    print("x is not the largest number.")


x = 30
y = 50
z = 10
if x > y or x > z:
    print("x is at least larger than one  number.")
else:
    print("x is the smallest number.")


x = 10
y = 20
z = 30
if not(x > y or x > z):
    print("x is not the largest number.")
else:
    print("x is not the smallest number.")