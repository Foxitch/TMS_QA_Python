# 1. Сохранить данные о машине в файл в json формате
# 2. Доделать классы машин, сделав их датаклассом. Сделать возможность сравнения по году выпуска машин
# 3. Загрузить машины из json файла
# 4. Написать функцию, которая создает несколько машин и сохраняет их в файл, если файла нет или он пустой


from dataclasses_json import dataclass_json
from dataclasses import dataclass, field

""" Initialize DataClass """


@dataclass_json
@dataclass(order=False)
class DataCar:
    name: str = field(compare=False)
    color: str = field(compare=False)
    year: int = field(compare=True)
    speed_limit: int = field(compare=False)

    def __post_init__(self):
        if not isinstance(self.name, str):
            raise ValueError('name must be a string')
        if not isinstance(self.color, str):
            raise ValueError('color must be a string')
        if not isinstance(self.year, int):
            raise ValueError('year must be an integer')
        if not isinstance(self.speed_limit, int):
            raise ValueError('speed_limit must be a integer')

    def __gt__(self, other):
        return self.year > other.year

