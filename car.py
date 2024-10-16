class Car:


    def __init__(self, model, year_of_manufacture, engine_capacity, price, mileage, wheels = 4):
        self.model = model
        self.year_of_manufacture = year_of_manufacture
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.wheels = wheels

vehicle1 = Car('Ford', 2000, 500, 10000, 10)

class Truck(Car):


    def __init__(self, model, year_of_manufacture, engine_capacity, price, mileage, wheels = 4):
        super().__init__(model, year_of_manufacture, engine_capacity, price, mileage, wheels = 8)

    def description(self):
        """Получение описания грузовика"""
        description = (f"Название модели - {self.model}, год выпуска - {self.year_of_manufacture}, "
                         f"объем двигателя - {self.engine_capacity}, цена - {self.price}, пробег - {self.mileage}, "
                        f"количество колес - {self.wheels}")
        print(description)


vehicle2 = Truck('Scania', 2010, 700, 20000, 5)

vehicle2.description()