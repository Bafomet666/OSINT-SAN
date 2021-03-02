from typing import List, Callable, Dict, Any

from core.params.params import Parameter
from core.dependency import Dependency

from dataclasses import dataclass, field

from core.utils import console


@dataclass
class Plugin:
    name: str
    description: str
    run_command: Callable

    dependencies: List[Dependency] = field(default_factory=list)
    parameters: List[Parameter] = field(default_factory=list)

    def check_dependencies(self) -> List[Dependency]:
        """Проверка зависимостей

        :return: Список неустановленных зависимостей
        :rtype: List[Dependency]
        """
        unresolved_dependencies = []
        for dep in self.dependencies:
            if not dep.installed():
                unresolved_dependencies.append(dep)

        return unresolved_dependencies

    def ask_for_parameters(self) -> Dict[str, Any]:
        """Запрос параметра от юзера

        Запрошивает пользовательские данные, заданные в `parameters`

        :return: готовые пользовательские данные
        :rtype: Dict[str, Any]
        """
        parameters_value: Dict[str, Any] = {}

        for parameter in self.parameters:
            parameter_value = parameter.input()
            parameters_value[parameter.name] = parameter_value

        return parameters_value

    def run(self):
        """Основной запуск плагина

        Выполняет 3 основные итерации:
        1. Проверка зависимотей
        2. Запрос пользовательских данных
        3. Выполнение основной функции

        :return: результат команды, заданной в `run_command`
        :rtype: Any
        """
        unresolved_deps = self.check_dependencies()
        if unresolved_deps:
            for dep in unresolved_deps:
                print(dep.uninstalled_info_message())
        else:
            parameters = self.ask_for_parameters()
            if parameters:
                console.empty_lines(2)

            return self.run_command(**parameters)


plugin_WIP = Plugin(
    name="В разработке...",
    description="Плагин еще находится в разработке!",
    run_command=lambda: print("Плагин еще находится в разработке!"),
)

plugin_PRO = Plugin(
    name=f"Доступно в {console.red('PRO')} {console.green('версии....', end=False)}",
    description="Плагин еще находится в разработке!",
    run_command=lambda: print("Плагин еще находится в разработке!"),
)


if __name__ == '__main__':
    from core import params
    from core.dependency import Api, Package, Platform, Permission

    import settings

    def hello_port(port):
        print(f"Hello port {port}!")

    plugin = Plugin(
        name="Test Plugin",
        description="Test plugin",
        run_command=hello_port,
        dependencies=[
            Api(settings.shodan_api),
            Package("whoami"),
            Platform("Linux") + Platform("Windows"),
            Permission("user"),
        ],
        parameters=[params.PORT],
    )
    plugin.run()
