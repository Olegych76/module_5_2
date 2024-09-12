class House:

    def __init__(self, name, q_floor):
        self.name = name
        self.q_floor = q_floor

    def __len__(self):
        return self.q_floor

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.q_floor}"

    def go_to(self, new_floor):
        if new_floor == 0 or new_floor > self.q_floor:
            print('Нет такого этажа!')
            return
        for i in range(0, new_floor):
            print(i + 1)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

