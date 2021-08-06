class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_style, shirt_price):
        self.color = shirt_color
        self.size = shirt_size
        self.style = shirt_style
        self.price = shirt_price

    def change_price(self, new_price):
        self.price = new_price

    def discount(self, discount):
        return self.price*(1-discount)




new_shirt = Shirt('red', 'S', 'short sleeve', 15)

print(new_shirt.color)
print(new_shirt.style)

print(new_shirt.discount(.2))


t_shirt_collection = []
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)

t_shirt_collection.append(shirt_one)
t_shirt_collection.append(shirt_two)
t_shirt_collection.append(shirt_three)

for i in range(len(t_shirt_collection)):
    print(t_shirt_collection[i].color)
