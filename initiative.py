class Cheese:

    def __move(self, string):
        print(string)

    def _draw(self):
        print('ggg')


a = Cheese()
# a.__move()


class Cheese1(Cheese):
    def __init__(self):
        super().__init__()

    def test(self):
        self._draw()
        self.__move("string")


Cheese1().test()

