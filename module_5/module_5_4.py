class House():

    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, *args):
        self.name = args[0]
        self.number_of_floors = args[1]

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        return 'Не объект House'

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        return 'Не объект House'

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        return 'Не объект House'

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        return 'Не объект House'

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        return 'Не объект House'

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        return 'Не объект House'

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
            return self
        return 'Не число'

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self
        return 'Не число'

    def __radd__(self, value):
        if isinstance(value, int):
            self.number_of_floors = value + self.number_of_floors
            return self
        return 'Не число'

    def __sub__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors - value
            return self
        return 'Не число'

    def go_to(self, new_floor):
        if self.number_of_floors < new_floor and new_floor >= 0:
            print ("Такого этажа не существует")

        else:
            floor = 1
            while floor <= new_floor:
                print(floor)
                floor += 1


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)