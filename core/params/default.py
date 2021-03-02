import platform

from core.params.params import Parameter, Reason

import re

from core.utils import console

IP_REGEXP = re.compile(r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
DOMAIN_REGEXP = re.compile(r"^(((?!-))(xn--|_{1,1})?[a-z0-9-]{0,61}[a-z0-9]{1,1}\.)*(xn--)?([a-z0-9][a-z0-9\-]{0,60}|[a-z0-9-]{1,30}\.[a-z]{2,})$")


class Ip(Parameter):
    name = "ip"
    input_ask = f"Введите ip {console.arrow}"

    def validate(self, raw_value):
        if not re.match(IP_REGEXP, raw_value):
            return Reason("Айпи введен неверно!")


class Port(Parameter):
    name = "port"
    input_ask = f"Введите порт {console.arrow}"

    def convert(self, raw_value):
        return int(raw_value)

    def validate(self, raw_value):
        if not raw_value.isnumeric():
            return Reason("Порт не является числом!")
        elif int(raw_value) > 65535:
            return Reason("Порт больше 65535!")


class Domain(Parameter):
    name = "domain"
    input_ask = f"Введите домен {console.arrow}"

    def validate(self, raw_value):
        if not re.match(DOMAIN_REGEXP, raw_value):
            return Reason("Домен введен неверно!")


IP = Ip()
DOMAIN = Domain()
PORT = Port()
