from itertools import islice
from typing import Dict, Union, List, Tuple, Iterable

from dataclasses import dataclass, field

from core.plugin import Plugin
from core.utils import console

RUNNER = Union[Plugin, "Menu"]
OPTION_RUNNER = Tuple[int, RUNNER]


class OptionAlreadyExists(Exception):
    pass


@dataclass(frozen=True)
class Menu:
    name: str
    description: str

    option_menu: Dict[int, RUNNER] = field(default_factory=dict)
    banner: str = ""
    post_option_banner: str = ""
    option_exit: str = 99

    def add_option(
            self,
            option: int,
            value: RUNNER,
            overwrite: bool = False,
    ) -> None:
        if not overwrite and self.option_menu.get(option):
            raise OptionAlreadyExists

        self.option_menu[option] = value

    def new_options(self, runners: List[RUNNER]) -> None:
        self.option_menu.clear()
        for i, runner in enumerate(runners, start=1):
            self.option_menu[i] = runner

    @staticmethod
    def _build_one_line_represented_options(options: List[OPTION_RUNNER]) -> str:

        def colorize_option(option: int, text_slot: str) -> str:
            return console.blue('[ ') + console.red(option) + console.blue(" ] ") + console.green(text_slot)

        some = "   "
        for option, runner in options:
            option_string = colorize_option(option, runner.name)
            some += option_string + " " * 13

        return some

    @staticmethod
    def split_every(n: int, iterable: Iterable) -> List:
        i = iter(iterable)
        piece = list(islice(i, n))
        while piece:
            yield piece
            piece = list(islice(i, n))

    def build_options(self) -> str:
        options = self.option_menu.items()

        return "\n".join(
            self._build_one_line_represented_options(options_in_one_line)
            for options_in_one_line in self.split_every(3, options)
        )

    def show_banner(self,) -> None:
        console.clear_screen()
        print(self.banner)

    def run_plugin(self, plugin: Plugin) -> None:
        self.show_banner()

        print("==============================")

        try:
            plugin.run()
        except KeyboardInterrupt:
            self.show_banner()
            return

        print("==============================\n")

    def run_menu(self, menu: "Menu") -> None:
        menu.run()
        self.show_banner()

    def run(self):
        input_ask = console.blue(f"Выберите опцию, для выхода - {console.red(self.option_exit)} {console.arrow}")
        banner_options = self.build_options()

        self.show_banner()
        while True:
            print(banner_options)
            print(self.post_option_banner)
            console.empty_lines(2)

            try:
                option = input(input_ask)
                option = int(option)
            except KeyboardInterrupt:
                break
            except ValueError:
                continue

            if option == self.option_exit:
                break

            runner = self.option_menu.get(option)
            if not runner:
                self.show_banner()
                continue

            if isinstance(runner, Plugin):
                self.run_plugin(runner)

            elif isinstance(runner, Menu):
                self.run_menu(runner)

        console.clear_screen()


def main():
    from core import params
    from core.dependency import Api, Platform, Package
    import settings

    menu = Menu(
        name="test menu",
        description="test description",
        banner=f"""
    {console.green("=============")}
    {console.blue("TEST BANNER!")}
    {console.green("=============")}
    """
    )

    menu.add_option(1, Plugin(
        name="Первый плагин",
        description="description",
        run_command=lambda: print("Hello world1!"),
        dependencies=[
            Package("whoami"),
            Api(settings.shodan_api),
            Platform("Windows") + Platform("Linux"),
        ],
    ))
    menu.add_option(2, Plugin(
        name="Второй плагин",
        description="description2",
        run_command=lambda port: print(f"Hello world2! {port}"),
        parameters=[params.PORT],
    ))

    menu2 = Menu(
        name="Второе меню",
        description="abc",
        banner="""
======================
БАННЕР ПОД ВТОРОЕ МЕНЮ
======================
""",
        post_option_banner="""
=========================
БАННЕР ПОСЛЕ ОПЦИЙ, ПОНЯЛ
=========================
"""
    )
    menu2.add_option(3, Plugin(
        name="Plugin inside menu2",
        description="menu2 plugin",
        run_command=lambda ip, port: print(f"Hello {ip} on {port}!"),
        parameters=[params.IP, params.PORT],
    ))
    menu.add_option(3, menu2)

    menu.run()
