from math import pi, sqrt
from tkinter import *
from tkinter import ttk


class Figure:
    sides_count = 2
    color_error_message = False
    sides_error_message = False
    impossible_sizes = False
    def __init__(self, __color: tuple, *__sides):
        color = list(__color)
        sides = [*__sides]
        if self.__is_valid_sides(sides):
            self.__sides = sides
        else:
            self.__sides = [1] * self.sides_count
        if self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = color
        else:
            self.__color = [0, 0, 0]

    def get_color(self):
        return self.__color

    def __is_valid_color(self, a, b, c):
        if 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255:
            self.color_error_message = False
            return True
        else:
            self.color_error_message = True
            return False

    def set_color(self, *color):
        color = [*color]
        if self.__is_valid_color(color[0], color[1], color[2]):
            self.__color = color
            self.color_error_message = False
        else:
            self.color_error_message = True
            print('Invalid value')

    def __is_valid_sides(self, sides):
        if len(sides) == self.sides_count and all(isinstance(side, int) for side in sides):
            self.sides_error_message = False
            return True
        else:
            self.sides_error_message = True
            return False

    def get_sides(self):
        return self.__sides

    def set_sides(self, *sides):
        sides = [*sides]
        if self.__is_valid_sides(sides):
            self.__sides = sides
            self.color_error_message = False
        else:
            self.color_error_message = True
            print('Invalid value')

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)
        self._radius = round(self.get_sides()[0] / (2 * pi), 2)

    def get_square(self):
        return round(self._radius * self._radius * pi, 2)

    def draw_circle(self):
        canvas.create_oval(50, 50, 300, 300, tags="figure", fill=convert_color(self.get_color()))
        text_radius = f'Radius: {self._radius}'
        text_perimeter = f'Perimeter: {self.get_sides()[0]}'
        text_square = f'Square: {self.get_square()}'
        text_color = f'Color: {self.get_color()}'
        canvas.create_text(330, 50, text=text_radius, tags="tip_text", anchor=NW, **tip_font)
        canvas.create_text(330, 75, text=text_perimeter, tags="tip_text", anchor=NW, **tip_font)
        canvas.create_text(330, 100, text=text_square, tags="tip_text", anchor=NW, **tip_font)
        canvas.create_text(330, 125, text=text_color, tags="tip_text", anchor=NW, **tip_font)


class Triangle(Figure):
    sides_count = 3
    impossible_sizes = False

    def __init__(self, color: tuple, *sides):
        super().__init__(color, *sides)
        if not self.additional_sides_check():
            self.set_sides(1, 1, 1)

    def get_square(self):
        a, b, c = self.get_sides()
        p = (a + b + c) / 2
        return round(sqrt(p * (p - a) * (p - b) * (p - c)), 2)

    def additional_sides_check(self):
        if max(self.get_sides()) < sum(self.get_sides()) - max(self.get_sides()) and sum(self.get_sides()) != 3:
            self.impossible_sizes = False
            return True
        else:
            self.impossible_sizes = True
            return False

    def draw_triangle(self):
        max_side = max(self.get_sides())
        multiplier = 250 / max_side
        c_square = self.get_square() * multiplier * multiplier
        c_max_side = 250
        c_tr_height = c_square / c_max_side * 2
        p2_y = 300 - c_tr_height
        other_sides = list(self.get_sides())
        other_sides.remove(max_side)
        d2_x = sqrt(other_sides[0] * other_sides[0] * multiplier * multiplier - c_tr_height * c_tr_height)
        p2_x = 50 + d2_x
        points = (
            (50, 300),
            (p2_x, p2_y),
            (300, 300),
        )
        canvas.create_polygon(*points, tags="figure", fill=convert_color(self.get_color()), outline="#000000")
        text_square = f'Square: {self.get_square()}'
        text_color = f'Color: {self.get_color()}'
        text_sides = f'Sides: {self.get_sides()}'
        canvas.create_text(330, 75, text=text_square, tags="tip_text", anchor=NW, **tip_font)
        canvas.create_text(330, 100, text=text_color, tags="tip_text", anchor=NW, **tip_font)
        canvas.create_text(330, 125, text=text_sides, tags="tip_text", anchor=NW, **tip_font)


class Cube(Figure):
    sides_count = 12

    def __init__(self, color: tuple, *sides):
        cube_sides = self.cube_check_sides(*sides)
        super().__init__(color, *cube_sides)

    def cube_check_sides(self, *sides):
        sides = [*sides]
        if len(sides) == 1:
            return sides * self.sides_count
        else:
            return sides

    def get_volume(self):
        sides = self.get_sides()
        return sides[0] * sides[1] * sides[2]

    def draw_cube(self):
        canvas.create_rectangle(50, 100, 220, 270, tags="figure", fill=convert_color(self.get_color()))
        points_1 = ((270, 60), (110, 60), (50, 100), (220, 100))
        canvas.create_polygon(*points_1, tags="figure", fill=convert_color(self.get_color()), outline="#000000")
        points_2 = ((270, 60), (270, 210), (220, 270), (220, 100))
        canvas.create_polygon(*points_2, tags="figure", fill=convert_color(self.get_color()), outline="#000000")
        text_side = f'Side: {self.get_sides()[0]}'
        text_volume = f'Volume: {self.get_volume()}'
        text_color = f'Color: {self.get_color()}'
        canvas.create_text(330, 75, text=text_side, tags="tip_text", anchor=NW, **tip_font)
        canvas.create_text(330, 100, text=text_volume, tags="tip_text", anchor=NW, **tip_font)
        canvas.create_text(330, 125, text=text_color, tags="tip_text", anchor=NW, **tip_font)


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


def convert_color(color):
    return '#%02x%02x%02x' % tuple(color)


def canvas_draw():
    hide_errors()
    inc_figure = figure.get()
    inc_params = params.get()
    if not inc_params:
        show_error('Empty field')
        return False
    str_ = str(inc_params).replace(':', ',')
    str_ = str_.translate({ord(i): None for i in '(){}[],\''})
    str_ = str_.split()

    if len(str_) < 4:
        show_error('Invalid value')
        return False

    parses_str = []
    for val in str_:
        try:
            parses_str.append(int(val))
        except ValueError:
            parses_str = 'Value is not integer'
            show_error(parses_str)
            return False

    canvas.delete("figure")
    canvas.delete("tip_text")

    if inc_figure == 'Circle':
        d_circle = Circle((parses_str[0], parses_str[1], parses_str[2]), *parses_str[3::])  # (200, 200, 100), 10
        check_figure_errors(d_circle)
        d_circle.draw_circle()

    if inc_figure == 'Triangle':
        d_triangle = Triangle((parses_str[0], parses_str[1], parses_str[2]),*parses_str[3::])  # (200, 150, 250), 2, 50, 51
        check_figure_errors(d_triangle)
        d_triangle.draw_triangle()

    if inc_figure == 'Cube':
        d_cube = Cube((parses_str[0], parses_str[1], parses_str[2]), *parses_str[3::])  # (200, 150, 250), 2
        check_figure_errors(d_cube)
        d_cube.draw_cube()


def show_error(error):
    params_error_message['text'] = error


def hide_errors():
    params_error_message['text'] = ''
    color_error_message['text'] = ''
    sides_error_message['text'] = ''
    sides_error_message.place(x=160, y=100)

def check_figure_errors(Obj):
    if Obj.color_error_message:
        color_error_message['text'] = f'Invalid color values, color is set to {Obj.get_color()}'
        sides_error_message.place(x=160, y=120)
    if Obj.sides_error_message:
        sides_error_message['text'] = f'Invalid sides values, sides is set to {Obj.get_sides()[0]}'
    if Obj.impossible_sizes:
        sides_error_message['text'] = f'Invalid sides values, sides is set to {Obj.get_sides()[0]}'


window = Tk()
window.title("Figures")
window.geometry("500x600")

figures = ["Circle", "Triangle", "Cube"]
position = {"padx": 6, "pady": 6, "anchor": NW}
tip_font = {'fill': "#000000", 'font': ("Roboto", 9)}

figure = StringVar(value=figures[0])  # Значение по умолчанию

header_1 = ttk.Label(text='Select figure', font=("Roboto", 12))
header_1.pack(**position)

for figure_radio_btn in figures:
    ttk.Radiobutton(text=figure_radio_btn, value=figure_radio_btn, variable=figure).pack(**position)

header_2 = ttk.Label(text='Params:', font=("Roboto", 12))
header_2.place(x=160, y=6)

params = ttk.Entry()
params.place(height=24, width=150, x=160, y=40)

tip_2 = ttk.Label(text='(255, 255, 255), a, b, c ...', font=("Roboto", 7))
tip_2.place(x=160, y=66)

color_error_message = ttk.Label(text='', font=("Roboto", 11), foreground="red")
color_error_message.place(x=160, y=100)

sides_error_message = ttk.Label(text='', font=("Roboto", 11), foreground="red")
sides_error_message.place(x=160, y=100)

params_error_message = ttk.Label(font=("Roboto", 9), foreground="red")
params_error_message.place(x=160, y=86)

btn_draw = ttk.Button(window, text="Draw figure", command=canvas_draw)
btn_draw.place(height=24, width=150, x=344, y=40)

canvas = Canvas(window, width=500, height=400)
canvas.place(x=0, y=200)

window.mainloop()
