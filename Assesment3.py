Fruits = ["apple", "banana", "cherry", "Mango"]
print(Fruits)
Fruits[-1] = "Pineapple"
print(Fruits)


colors = ["red", "blue", "green"]
print(colors)
colors[-2] = "yellow"
print(colors)
colors.append("purple")
print(colors)
colors.insert(0, "orange")
print(colors)



shopping_list = ["milk", "eggs", "bread", "candy", "butter"]
print(shopping_list)
shopping_list.remove("candy")
print(shopping_list)
shopping_list.pop(-1)
print(shopping_list)
print(len(shopping_list))


scores = [10, 20, 30, 40, 50]
print(scores)
for score in scores:
    print(score * 2)
    sum(scores)


todo_list = []
todo_list.append("Finish homework")
todo_list.append("Clean room")
todo_list.append("cook dinner")
print(todo_list)
todo_list.sort()
print(todo_list)