# 1. Реализовать абстрактный класс машины (придумайте какие методы у машины есть, какие нужно
# у всех дочерних классов переопределять, а какие будут общие с готовой реализацией)
# 2. Реализовать несколько классов разных марок машин, наследуемых от базовой машины.
# Переопределить абстрактные методы, свойства.
# Придумать новые методы, которые есть только в конкретных марках машин.
# 3. Реализовать класс абстрактный класс самолета.
# Должно быть как минимум один или несколько одноименных атрибутов класса машины.
# Тоже самое из п.1
# 4. Реализовать несколько классов разных марок самолетов. Тоже самое из п.2
# 5. Создать несколько экземпляров каждой машины, каждого самолета, вызвать различные методы у этих объектов.
# «Поиграться», скажем так:
# А затем сделать коллекцию из этих объектов и через цикл пройтись по каждому из этих объектов
# и вызвать те методы, которые есть во всех классах.

from abc import abstractmethod, ABC


class Car(ABC):

    def __init__(self, max_speed: int):
        self.max_speed = max_speed

    def move(self):
        print(f'I am going, max speed is {self.max_speed}')

    @staticmethod
    def to_break():
        print('I crashed')

    def acceleration(self, speed: int):
        current_speed = min(self.max_speed, speed)
        print(f'My current speed is {current_speed}')

    @abstractmethod
    def shift_type(self):
        pass

    @abstractmethod
    def type(self):
        pass


class Bmw(Car):

    def shift_type(self):
        print('Bmw has automate shift type')

    @staticmethod
    def oil(oil_level):
        if oil_level == 0:
            print('...crickets crackling...')
        elif oil_level > 0:
            print('ora-ora-ora')

    def type(self):
        print('My type is Gold')


bmw = Bmw(100)


class Nissan(Car):

    def info(self):
        print('i am better than bmw')

    def shift_type(self):
        print(f'Nissan has manual shift type')

    def type(self):
        print('My type is Racing')


nissan = Nissan(120)

#################################################


class Plane:

    def __init__(self, height: int, coast: int, passengers: int, max_speed: int):
        self.max_height = 1000
        self.height = height
        self.coast = coast
        self.passengers = passengers
        self.max_speed = max_speed

    @abstractmethod
    def type(self):
        pass

    @abstractmethod
    def plane_type(self):
        pass

    def info(self):
        print(f'Max height is {self.max_height}, planes coast is {self.coast}, passengers count is {self.passengers}')


class Boeing(Plane):

    def type(self):
        print('My type is passenger')

    @staticmethod
    def ticket_coast(ticket: float):
        print(f'Ticket coast is {ticket}')


boeing = Boeing(1000, 1000000, 150, 300)


class BusinessJetta(Plane):

    def type(self):
        print('My type is business')

    @staticmethod
    def sputnik_internet():
        print('I have sputnik internet')


businessjetta = BusinessJetta(500, 1500000, 20, 250)


lst = [bmw, nissan, boeing, businessjetta]
for i in lst:
    i.type()

















