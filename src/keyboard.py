from src.item import Item


class MixinLang:
    """Класс-миксин по хранению и изменению раскладки клавиатуры"""

    languages = ["EN", "RU"]

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        self.__language = self.languages[0]

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = self.languages[1]
            return self
        else:
            self.__language = self.languages[0]
            return self


class Keyboard(MixinLang, Item):
    """Класс для товара клавиатура"""
    pass
