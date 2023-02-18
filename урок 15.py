#Урок No15. 
#Задание No1: 

class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

Autobus = Transport('Renaul Logan', 180, 12)
print(f'Название автомобиля: {Autobus.name} Скорость: {Autobus.max_speed} Пробег: {Autobus.mileage}')

#Задание No2: 

class Transport:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

class Autobus(Transport):
       
    def seating_capacity(self):
        return f"Вместимость одного автобуса {self.name}: 50 пассажиров"

bus = Autobus('Renaul Logan', 180, 12)
print(bus.seating_capacity())















