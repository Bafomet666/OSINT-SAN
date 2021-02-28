from typing import Any, Union, Optional

from dataclasses import dataclass, field

Reason = str


class ValidationError(Exception):
    pass


@dataclass
class Parameter:
    name: str = field(init=False)
    input_ask: str = field(default="", init=False)

    def ask(self) -> Any:
        """Получение данных с пользователя и валидация данных.

        Основной метод получения данных с пользователя.
        Происходит сбор в трех этапах:
        1. Сам сбор сырого значения (метод `collect()`)
        2. Валидация (метод 'validate()')
        3. Конвертация в нужный тип данных (метод 'convert()')
        Все эти три метода можно перегружать в случае необходимости.

        :return: полученные и провалидированные данные с пользователя.

        :raises: ValidationError, в случае, если валидация произошла неудачно.
        """
        raw_value = self.collect()

        reason = self.validate(raw_value)
        if reason:
            raise ValidationError(reason)

        return self.convert(raw_value)

    def collect(self) -> str:
        """Сбор пользовательского ввода в сыром виде

        Сбор данных либо из `stdin`, либо же как-то по другому
        При необходимости спокойно перегружается.

        :return: значения из пользовательского ввода
        :rtype: str
        """
        return input(self.input_ask)

    def convert(self, raw_value: str) -> Any:
        """Конвертация провалидированного значения в необходимый тип данных.

        :param raw_value:
        :type raw_value: str
        :return: готовое значение с необходимым типом
        """
        return raw_value

    def validate(self, raw_value: str) -> Union[None, Reason]:
        """Валидация пользовательских данных

        :param raw_value: полученное от ввода пользователя значение
        :type raw_value: str

        :return: Текст ошибки в случае неправильной конвертации
        :rtype: None если была ошибка, иначе Reason (str)
        """
        pass
