cart = ["apples", "bananas", "cherries"]
print(cart)
cart.append("donuts")
cart.append("milk")
cart.append("eggs")
print(cart)

cart.remove("cherries")
cart.pop(1)
print(cart)
cart.pop()
cart.append("bananas")
cart.append("bananas")
print(cart)
cart.sort()
print(cart)

fruit=cart[0:3]
print(fruit)

count=cart.count("bananas")
print(count)

squares = []
for i in range (1,11):
    squares.append(i**2)
print(squares)

# list comprehension
squares2 = [i**2 for i in range(1,11)]
print(squares2)

squares_even = [i**2 for i in range(1,11) if i%2==0]
print(squares_even)

cart2 = [item for item in cart if item.startswith('b')]
print(cart2)

inventory = [0]*10
inventory[4] = 100
print(inventory)

book_genres={"Romance"}
book_genres.add("Science Fiction")
book_genres.add("Mystery")
print(book_genres)
aset=set()

lst=[1,1,2,2,3,3,4,4,5,5]
unique = set(lst)
print(unique)

fav_snacks = {"Jamey":"Chocolate", "Bradley":"Up the butt", "Dan":"No sleep", "Blaise":"Femboys"}
Bradley=fav_snacks["Bradley"]
# print(Bradley)

for value in fav_snacks:
    print(fav_snacks[value])

for key, value in fav_snacks.items():
    print(key, value)

if "Jack" in fav_snacks:
    print(fav_snacks["Jack"])
else:
    fav_snacks["Jack"]="Ice Cream"
