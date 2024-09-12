class Product:
    def __init__(self, name: str, weight: float, category: str):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        result = f'{self.name}, {self.weight}, {self.category}'
        return result


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        file = open(self.__file_name, 'r')
        result = file.read()
        file.close()
        return result

    def add(self, *products: Product):
        file_products = self.get_products().split('\n')
        names = []

        for f_product in file_products:
            name = f_product.split(', ')[0]
            names.append(name)

        file_w = open(self.__file_name, 'a')

        for product in products:
            if not product.name in names:
                file_w.write(product.__str__() + '\n')
            else:
                print(f'Продукт {product.name} уже есть в магазине')

        file_w.close()



s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) # __str__

s1.add(p1, p2, p3)

print(s1.get_products())

