class Animal:
    alive = True  # живой
    fed = False  # накормленый

    def __init__(self, name : str):
        self.name = name


    def eat(self, food):
        if food.edible:
            print(F'{self.name} сьел {food.name}')
            self.fed = True
        else:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False


class Plant:
    edible = False  # съедобность

    def __init__(self, name : str):
        self.name = name



class Mammal(Animal):
    pass

class Predator(Animal):
    pass



class Flower(Plant):
    pass

class Fruit(Plant):
      edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

# Волк с Уолл-Стрит
# Цветик семицветик
# True
# False
# Волк с Уолл-Стрит не стал есть Цветик семицветик
# Хатико съел Заводной апельсин
# False
# True
