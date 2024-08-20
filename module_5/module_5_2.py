class House():
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor and new_floor >= 0:
            print ("Такого этажа не существует")

        else:
            floor = 1
            while floor <= new_floor:
                print(floor)
                floor += 1


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))