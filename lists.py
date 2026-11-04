letters = ['a', 'b', 'c',]
matrix = [[0, 1], [2, 3]]
zeroes = [0] * 5
combined = zeroes + letters
numbers = list(range(20))
chars = list('Hello World')
print(len(chars))



numbers = ['a', 'b', 'c', 'd']
numbers[0] = 'A'
print(numbers[0:3])
print(numbers[::2])


Ateeyah = list(range(20))
print(Ateeyah[::-1])


roblox = [1, 2, 3, 89, 89, 89, 89, 89,]
first, *other, last = roblox
print(first, last)
print(other)
first = roblox[0]
second = roblox[1]
third = roblox[2]


letter = ["a", "b", "c"]

for index, letter in enumerate(letter):
    print( index, letter)


    letters = ["a", "b", "c"]
#Add
letters.append("d")
letters.insert(0, "-")


#Remove
letters.pop(0)
letters.remove("b")
del letters[0:3]
letters.clear()
print(letters)



letters = ["a", "b", "c"]
letters.count("d")
if "d" in letters:
 print(letters.index("d"))
