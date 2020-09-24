# про наследование еще не было занятия, но оно напрашивалось


class Animal:
    animal_list = []  # заводим список всех животных
    sound = '*silence*'  # на случай появления на ферме рыб

    def __init__(self, name, gender=None, weight=None):
        self.name = name
        self.gender = gender
        self.weight = weight
        self.animal_list.append(self)

    def eats(self, food):
        self.weight += food / 10  # не вся еда идет в вес

    def makes_sound(self):
        print(self.sound)


class Bird(Animal):
    eggs = 0

    def lays_egg(self):
        if self.gender == 'F':
            self.eggs += 1
        else:
            print(f'{self.name} refuses to lay eggs. He is a boy')

    def collect_eggs(self):
        if self.eggs:
            print(f'{self.name} gives {self.eggs} egg{"s" if self.eggs > 1 else ""}')
            self.eggs = 0
        else:
            print('No eggs')


class DairyAnimal(Animal):
    milk_inside = 0

    def makes_milk(self, amount=1):
        if self.gender == 'F':
            self.milk_inside += amount
        else:
            print(f'{self.name} refuses to make milk. He is a boy')

    def milk(self):
        if self.milk_inside:
            print(f'{self.name} gives {self.milk_inside} liter{"s" if self.milk_inside > 1 else ""} of milk')
            self.milk_inside = 0
        else:
            print('No milk')        


class Goose(Bird):
    species = 'goose'
    sound = 'Honk'


class Chicken(Bird):
    species = 'chicken'

    def makes_sound(self):
        if self.gender == 'M':
            print('Cock-a-doodle-doo')
        else:
            print('Cluck')


class Duck(Bird):
    species = 'duck'
    sound = 'Quack'


class Cow(DairyAnimal):
    species = 'cow'
    sound = 'Moooo'


class Sheep(Animal):
    species = 'sheep'
    sound = 'Baaaa'
    wool = 0

    def grows_wool(self, amount=1):
        self.wool += amount

    def shear(self):
        if self.wool:
            print(f'{self.name} gives {self.wool} kilogramm{"s" if self.wool > 1 else ""} of wool')
            self.wool = 0
        else:
            print('No wool yet')


class Goat(DairyAnimal):
    species = 'goat'
    sound = 'Bleat'


gray = Goose('Серый', 'M', 5)
white = Goose('Белый', 'M', 6)
manka = Cow('Манька', 'F', 200)
barashek = Sheep('Барашек', 'M', 50)
koko = Chicken('Ко-Ко', 'F', 2)
kukareku = Chicken('Кукареку', 'M', 2)
roga = Goat('Рога', 'F', 25)
kopyta = Goat('Копыта', 'F', 26)
kryakva = Duck('Кряква', 'F', 3)

# примеры взаимодействия
print('Гусь говорит:', end=' ')
gray.makes_sound()
print(f'Серый весит {gray.weight} кило')
gray.eats(1)
print(f'Серый весит после еды {gray.weight} кило')
gray.lays_egg()
print()
print('Корова говорит:', end=' ')
manka.makes_sound()
manka.makes_milk(10)
manka.milk()
print()
print('Овечка говорит:', end=' ')
barashek.makes_sound()
manka.eats(3)
barashek.grows_wool(5)
barashek.shear()
barashek.shear()
print()
print('Курочка говорит:', end=' ')
koko.makes_sound()
print('Петушок говорит:', end=' ')
kukareku.makes_sound()
for _ in range(3): koko.lays_egg()
kukareku.lays_egg()
koko.collect_eggs()
koko.lays_egg()
koko.collect_eggs()
print()

# Задание 2
total_weight = 0
max_weight = ['', 0]
for animal in Animal.animal_list:
    total_weight += animal.weight
    if animal.weight > max_weight[1]:
        max_weight = [animal.name, animal.weight]
print(f'Общий вес животных: {total_weight} килограмм')
print(f'Самое тяжелое животное: {max_weight[0]} - {max_weight[1]} килограмм')
