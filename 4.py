class Car:
    speed: int
    color: str
    name: str
    is_poliсe: bool

    def go(self):
        return print('Машина поехала!')

    def stop(self):
        return print('Машина остановилась!')

    def turn(self, direction):
        print(f'Машина движется {direction}!')

    def show_speed(self):
        pass


class TownCar(Car):
    speed = 60
    color = 'Black and blue'
    name = 'Renault'
    is_poliсe = False

    def show_speed(self, speed):
        if speed > 60:
            return print(f'Превышена допустимая скорость в {self.speed} км/час')


class SportCar(Car):
    speed = 100
    color = 'Red'
    name = 'Lamborghini'
    is_poliсe = False


class WorkCar(Car):
    speed = 40
    color = 'White'
    name = 'Ford'
    is_poliсe = False

    def show_speed(self, speed):
        if speed > 40:
            return f'Превышена допустимая скорость в {self.speed} км/час'


class PoliceCar(Car):
    speed = 70
    color = 'Blue and white'
    name = 'Lada'
    is_poliсe = True


town_car = TownCar()
print(town_car.name, town_car.color)
print(town_car.go())
print(town_car.stop())
print(town_car.turn('налево'))
print(town_car.show_speed(70))

sport_car = SportCar()
print(sport_car.name, sport_car.color)
print(sport_car.go())
print(sport_car.stop())
print(sport_car.turn('прямо'))

work_car = WorkCar()
print(work_car.name, work_car.color)
print(work_car.go())
print(work_car.stop())
print(work_car.turn('направо'))
print(work_car.show_speed(50))

police_car = PoliceCar()
print(police_car.name, police_car.color)
print(police_car.go())
print(police_car.stop())
print(police_car.turn('назад'))

# почему-то при выведении результатов через строчку None
# пока не понимаю, с чем это связано
