from typing import Any

# Первый класс
class Whatsapp:
    def __init__(self, messages: int, missed_messages: int, phone_calls: int, missed_calls: int, settings: Any):
        """
        Создание и подготовка к работе Whatsapp
        :param messages: Количество диалогов
        :param missed_messages: Количество непрочитанных сообщений
        :param phone_calls: Количество звонков
        :param missed_calls: Количество пропущенных звонков
        :param settings: Default настройки
        """
        self.messages = messages
        self.missed_messages = missed_messages
        self.phone_calls = phone_calls
        self.missed_calls = missed_calls
        self.settings = settings

    def send_message(self, message: str) -> str:
        """
        Отправить сообщение.

        :param message: Сообщение
        :return: message
        """
        ...

    def make_call(self, phone_number: str) -> int:
        """
        Позвонить по заданному номеру.
        :return: Количество минут разговора
        """
        ...

    def take_photo(self, phone_number: str):
        """
        Сделать фотографию и отправить кому-то
        :param phone_number: кому хотим отправить
        :return: фотография в виде отправленного сообщения
        """
        ...

    def geoposition(self, phone_number: str):
        """
        Поделить геопозицией
        :param phone_number: с кем хотим поедлиться
        :return: ссылка на Гугл карты
        """
        ...

# Второй класс
class CoffeeMachine:
    def __init__(self, water: int, ):

