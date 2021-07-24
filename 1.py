import time


class TrafficLight:
    __traffic_color = 'red', 'yellow', 'green'

    def running(self):
        self.__traffic_color = 'red'
        print('Горит красный!')
        time.sleep(7)
        self.__traffic_color = 'yellow'
        print('Горит желтый!')
        time.sleep(2)
        self.__traffic_color = 'green'
        print('Горит зеленый!')
        time.sleep(15)


my_light = TrafficLight()
my_light.running()
