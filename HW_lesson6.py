"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов,
и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
import time

class TraficLight:
    color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        item = 0
        while item < 3:
            print(f"Cейчас горит {TraficLight.color[item]} сигнал светофора")
            if item == 0:
             time.sleep(7)
            elif item == 1:
                time.sleep(2)
            elif item == 2:
                time.sleep(10)
                item = -1
            item += 1

roadlight = TraficLight()
roadlight.running()

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
class Road:
    def __init__(self, _lenght, _width):
        self._lenght = _lenght
        self._width = _width

    def massa(self, depth=1):
        return self._width * self._lenght * depth * 25

weight = Road(100, 5)
print(f'Масса асфальта, необходимого для покрытия дорожного полотна - {weight.massa(5)} кг ({weight.massa(5)/1000} т)')

"""
3. Реализовать базовый класс Worker (работник),
в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь,
содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            "wage": wage,
            "bonus": bonus
        }
class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')

worker1 = Position('Alex', 'Ivanov', 'Director', 100000, 50000)
print(f'Полное Имя {worker1.get_full_name()}')
print(f'Доход с учетом премии {worker1.get_total_income()} $')

"""
4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = False

    def go(self):
        return f'{self.name} is going'

    def stop(self):
        return f'{self.name} is stopped'

    def turnleft(self):
        return f'{self.name} turn left'

    def turnright(self):
        return f'{self.name} turn right'

    def showspeed(self):
        return f'{self.name} moves with speed {self.speed} km/h'

class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if self.speed > 60:
            return f'Speed of {self.name} exceeded the speed limit for town car'
        return f'Speed of {self.name} is normal'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
         super().__init__(speed, color, name, is_police)

    def showspeed(self):
        if self.speed > 40:
            return f'Speed of {self.name} exceeded the speed limit for work car'
        return f'Speed of {self.name} is normal'

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is policeman'
        return f'{self.name} is not policeman'

ferrary = SportCar(150, 'Red', 'Ferrary', False)
toyota = TownCar(100, 'White', 'TOYOTA', False)
nisan = WorkCar(35, "black", 'NISAN', False)
oka = PoliceCar(10, "Rga", 'OKA', True)

print(f'Speed {toyota.color} {toyota.name} is {toyota.speed}')
print(toyota.showspeed())
print(f'{toyota.name} is police? {toyota.is_police}')

print(f'Speed {ferrary.color} {ferrary.name} is {ferrary.speed}')
print(ferrary.showspeed())
print(f'{ferrary.name} is police? {ferrary.is_police}')

print(f'Speed {nisan.color} {nisan.name} is {nisan.speed}')
print(nisan.showspeed())
print(f'{nisan.name} is police? {nisan.is_police}')

print(f'Speed {oka.color} {oka.name} is {oka.speed}')
print(oka.showspeed())
print(f'{oka.name} is police? {oka.is_police}')

print(ferrary.go())
print(toyota.stop())
print(nisan.turnleft())
print(oka.turnright())

""""
5. Реализовать класс Stationery (канцелярская принадлежность).
Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.”
Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""





class Stationery:
    def __init__(self, title = "1"):
        self.title = title

    def draw(self):
        return 'Запуск отрисовки'

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return f'Рисуем ручкой. {self.title}'

class Pencil(Stationery):

    def draw(self):
        return f'Рисуем карандашем. {self.title}'

class Handle(Stationery):

    def draw(self):
        return f'Рисуем маркером. {self.title}'


a = Pen("Ручка")
b = Pencil("Карандаш")
c = Handle("Маркер")
print(a.draw())
print(b.draw())
print(c.draw())