class Cat:
    print()
    def __init__(self, name = None):
        self.name = name
        self.weight = 4
        self.height = 28
        print()
        print(f"Meow Meow")
        print(f'Hi! my name is {name}')
        print('    There about me :')


    def add_weight(self):
        self.weight += 1.4


print("-"*15, "Tom", "-"*16, sep="")
Tom = Cat(name = "Tom")
Tom.add_weight()
Tom.add_weight()
print(f"Weight Tom - {Tom.weight} kilograms")
print(f"Height Tom - {Tom.height} centimeters")

print()
print('-'*34)
print()

print("-"*15, "Keti", "-"*15, sep="")
Keti = Cat(name = "Keti")
Keti.add_weight()
print(f"Weight Keti - {Keti.weight} kilograms")
print(f"Height Keti - {Keti.height} centimeters")

print()
print("-"*34)