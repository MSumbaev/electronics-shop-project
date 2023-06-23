from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []
    path_file_csv = "src/items.csv"

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name

    def __add__(self, other):
        """Cложение экземпляров класса по количеству товара в магазине"""
        if not issubclass(other.__class__, self.__class__):
            raise ValueError("Складывать можно только объекты Item и дочерние от них.")
        return self.quantity + other.quantity

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, first: str):
        if len(first) < 10:
            self.__name = first
        else:
            print("Exception: Длина наименования товара превышает 10 символов.")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= Item.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """Класс-метод, инициализирующий экземпляры класса `Item` данными из файла _src/items.csv
        При инициализации экземпляров из файла старые экземпляры удаляются."""

        cls.all.clear()

        try:
            with open(Item.path_file_csv, encoding="cp1251") as f:
                reader = DictReader(f)

                if len(reader.fieldnames) < 3:
                    raise InstantiateCSVError("Файл items.csv поврежден")
                for field in reader.fieldnames:
                    if field not in ["name", "price", "quantity"]:
                        raise InstantiateCSVError("Файл items.csv поврежден")

                for line in reader:
                    cls(line["name"], line["price"], line["quantity"])

        except FileNotFoundError:
            raise FileNotFoundError("Отсутствует файл item.csv")

    @staticmethod
    def string_to_number(number: str):
        """Статический метод, возвращающий число из числа-строки.
        Если есть буквы в number присваивает переменной значение = 0."""

        if isinstance(number, str):
            try:
                float(number)
            except ValueError:
                print("Данные не являются числом! Присвоено значение = 0")
                number = 0
            return int(float(number))
        else:
            print("Данные не являются строкой!")


class InstantiateCSVError(Exception):
    pass
