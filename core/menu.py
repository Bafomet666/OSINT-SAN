import os
from typing import Dict, Union, List, Iterator

from dataclasses import dataclass, field

from core.plugin import Plugin
from functools import lru_cache
# from core.params import Parameter

RUNNER = Union[Plugin, "Menu"]


class OptionAlreadyExists(Exception):
    pass


@dataclass
class Menu:
    name: str
    description: str

    option_menu: Dict[str, RUNNER] = field(default_factory=dict)
    banner: str = ""
    option_exit: str = "99"

    def add_option(
            self,
            option: str,
            value: RUNNER,
            overwrite: bool = False,
    ) -> None:
        if not overwrite and self.option_menu.get(option):
            raise OptionAlreadyExists

        self.option_menu[option] = value

    def clear_screen(self) -> None:
        os.system("clear")

    def _build_one_line_represented_options(
            self,
            options: List[Union[str, RUNNER]],
    ) -> str:
        for option, runner in options:
            option_string = f"[ {option} ] {runner.name}"

    @staticmethod
    def _collect_options(options_iter: Iterator, *, take: int = 3) -> List:
        options = []
        for i in range(take):
            try:
                option = next(options_iter)
            except StopIteration:
                break
            else:
                options.append(option)

        if not options:
            raise StopIteration

        return options

    @lru_cache(maxsize=1)
    def represent_options(self) -> str:
        option_iter = iter(self.option_menu.items())

        represented_options = []
        while True:
            try:
                options_on_one_line = self._collect_options(option_iter, take=3)
            except StopIteration:
                break
            represented_one_line = self._build_one_line_represented_options(options_on_one_line)
            represented_options.append(represented_one_line)

        return "\n".join(represented_options)

    def run(self):
        print(self.banner)
        while True:
            try:
                option = input(f"Выберите опцию, для выхода - {self.option_exit}")
            except KeyboardInterrupt:
                return

            if option == self.option_exit:
                return

            elif not self.option_menu.get(option):
                continue

            runner = self.option_menu.get(option)
            runner.run()


if __name__ == '__main__':
    from core import params

    menu = Menu(
        name="test menu",
        description="test description",
    )

    menu.add_option("1", Plugin(
        name="hello_world_1",
        description="description",
        run_command=lambda: print("Hello world1!"),
    ))
    menu.add_option("2", Plugin(
        name="hellow_world_2",
        description="descr",
        run_command=lambda port: print(f"Hello world2! {port}"),
        parameters=params.PORT,
    ))

    menu2 = Menu(
        name="Some name",
        description=" descro",
        banner="LOL BANNER",
    )
    menu2.add_option("3", Plugin(
        name="Plugin inside menu2",
        description="menu2 plrugin",
        run_command=lambda ip: print(f"Hello {ip}!"),
        parameters=params.IP,
    ))
    menu.add_option("3", menu2)

    menu.run()
