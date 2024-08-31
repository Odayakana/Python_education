class Horse:

    def __init__(self):
        self.x_distance = 0
        self.sound = 'Frrr'

    def run(self, dx: int):
        self.x_distance += dx


class Eagle:

    def __init__(self):
        self.y_distance = 0
        self.sound = 'I train, eat, sleep, and repeat'

    def fly(self, dy: int):
        self.y_distance += dy


class Pegasus(Horse, Eagle):

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(self.sound)


p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
